#!/usr/bin/env python3
"""Check exported STL parts against printer build volumes.

Automates the manual checklist items in
05_Checklists/printer_material_decision_checklist.md:
    - Does the part fit inside P1S build volume: 256 x 256 x 256 mm?
    - Does the part fit inside A1 mini build volume: 180 x 180 x 180 mm?

Usage:
    python scripts/check_build_volume.py [stl_directory]

Defaults to scanning instructions/docs/assets/stls/ if no directory is given.
"""

from __future__ import annotations

import argparse
import struct
import sys
from dataclasses import dataclass
from pathlib import Path

# Build volumes from 05_Checklists/printer_material_decision_checklist.md (mm).
PRINTERS = {
    "P1S": (256.0, 256.0, 256.0),
    "A1 mini": (180.0, 180.0, 180.0),
}


@dataclass
class StlInfo:
    path: Path
    triangle_count: int
    dimensions: tuple[float, float, float]  # (x, y, z) bounding box in mm


def _is_ascii_stl(data: bytes) -> bool:
    # Binary STL files are not required to avoid starting with "solid", but in
    # practice an ASCII file always starts with it (optionally followed by a
    # name) and decodes cleanly as text.
    if not data[:80].lstrip().lower().startswith(b"solid"):
        return False
    try:
        data[: 4096].decode("ascii")
    except UnicodeDecodeError:
        return False
    return True


def _parse_binary_stl(data: bytes) -> tuple[int, tuple[float, float, float]]:
    (triangle_count,) = struct.unpack_from("<I", data, 80)
    expected_size = 84 + triangle_count * 50
    if expected_size != len(data):
        raise ValueError(
            f"binary STL triangle count ({triangle_count}) does not match "
            f"file size (expected {expected_size} bytes, got {len(data)})"
        )

    min_v = [float("inf")] * 3
    max_v = [float("-inf")] * 3
    offset = 84
    for _ in range(triangle_count):
        # Skip the 12-byte normal vector; read the 3 vertices (9 floats).
        verts = struct.unpack_from("<9f", data, offset + 12)
        for i in range(3):
            x, y, z = verts[i * 3 : i * 3 + 3]
            min_v[0], max_v[0] = min(min_v[0], x), max(max_v[0], x)
            min_v[1], max_v[1] = min(min_v[1], y), max(max_v[1], y)
            min_v[2], max_v[2] = min(min_v[2], z), max(max_v[2], z)
        offset += 50

    dims = tuple(max_v[i] - min_v[i] for i in range(3))
    return triangle_count, dims  # type: ignore[return-value]


def _parse_ascii_stl(data: bytes) -> tuple[int, tuple[float, float, float]]:
    min_v = [float("inf")] * 3
    max_v = [float("-inf")] * 3
    triangle_count = 0
    for line in data.decode("ascii", errors="ignore").splitlines():
        line = line.strip()
        if line.startswith("facet normal"):
            triangle_count += 1
        elif line.startswith("vertex"):
            _, x, y, z = line.split()
            x, y, z = float(x), float(y), float(z)
            min_v[0], max_v[0] = min(min_v[0], x), max(max_v[0], x)
            min_v[1], max_v[1] = min(min_v[1], y), max(max_v[1], y)
            min_v[2], max_v[2] = min(min_v[2], z), max(max_v[2], z)

    dims = tuple(max_v[i] - min_v[i] for i in range(3))
    return triangle_count, dims  # type: ignore[return-value]


def read_stl(path: Path) -> StlInfo:
    data = path.read_bytes()
    if _is_ascii_stl(data):
        triangle_count, dims = _parse_ascii_stl(data)
    else:
        triangle_count, dims = _parse_binary_stl(data)
    return StlInfo(path=path, triangle_count=triangle_count, dimensions=dims)


def fits(dims: tuple[float, float, float], volume: tuple[float, float, float]) -> bool:
    # Both printer volumes here are cubes, so axis order doesn't matter — a
    # part fits if every bounding-box dimension is within the build volume.
    return all(d <= v for d, v in zip(sorted(dims), sorted(volume)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory",
        nargs="?",
        default="instructions/docs/assets/stls",
        help="Directory to scan for .stl files (default: instructions/docs/assets/stls)",
    )
    args = parser.parse_args()

    stl_dir = Path(args.directory)
    if not stl_dir.is_dir():
        print(f"Error: '{stl_dir}' is not a directory", file=sys.stderr)
        return 1

    stl_files = sorted(stl_dir.rglob("*.stl"))
    if not stl_files:
        print(f"No .stl files found under '{stl_dir}'")
        return 0

    header = f"{'Part':<40} {'Dimensions (mm)':<22} {'Triangles':>10}"
    for name in PRINTERS:
        header += f"  {name:>10}"
    print(header)
    print("-" * len(header))

    any_oversized = False
    for path in stl_files:
        try:
            info = read_stl(path)
        except Exception as exc:  # noqa: BLE001
            print(f"{path.name:<40} ERROR: {exc}")
            any_oversized = True
            continue

        dims_str = "x".join(f"{d:.1f}" for d in info.dimensions)
        row = f"{path.name:<40} {dims_str:<22} {info.triangle_count:>10}"
        for volume in PRINTERS.values():
            ok = fits(info.dimensions, volume)
            row += f"  {'OK' if ok else 'TOO BIG':>10}"
            any_oversized = any_oversized or not ok
        print(row)

    return 1 if any_oversized else 0


if __name__ == "__main__":
    raise SystemExit(main())
