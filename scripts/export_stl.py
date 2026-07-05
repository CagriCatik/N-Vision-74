#!/usr/bin/env python3
"""Batch-export SolidWorks parts/assemblies to STL via COM automation.

Drives a real, licensed SolidWorks installation through its COM API — this
does not reimplement any CAD kernel, so SolidWorks must be installed on the
machine running this script. Windows only.

Usage:
    python scripts/export_stl.py [source_directory] [output_directory]

Defaults to scanning 03_SolidWorks_Project/ and writing STLs into
instructions/docs/assets/stls/.

Smoke test (no real project parts required):
    python scripts/export_stl.py --smoke-test
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

try:
    import pythoncom
    import win32com.client
except ImportError:
    print(
        "pywin32 is required: pip install pywin32 (Windows only)",
        file=sys.stderr,
    )
    raise

# swDocumentTypes_e — stable across SolidWorks API versions.
SW_DOC_PART = 1
SW_DOC_ASSEMBLY = 2

# A SolidWorks-bundled sample part, used only for --smoke-test so the export
# pipeline can be verified before any real project parts exist.
SAMPLE_PART = Path(
    "C:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/data/graphics/Templates/sphere.sldprt"
)


def connect():
    """Attach to a running SolidWorks instance, or launch one.

    Uses plain late-bound Dispatch rather than gencache.EnsureDispatch:
    SolidWorks' COM server isn't ready to serve full type info immediately
    after launch, which makes EnsureDispatch's automatic makepy step fail.
    Late binding also means we deliberately avoid win32com.client.constants
    for SolidWorks-specific enums; every constant this script relies on is
    hardcoded above from the stable, publicly documented API values.
    """
    try:
        app = win32com.client.GetActiveObject("SldWorks.Application")
    except Exception:
        app = win32com.client.Dispatch("SldWorks.Application")

    # A freshly launched SolidWorks process isn't immediately ready to
    # service COM calls (splash screen, license check, etc.); poll a
    # lightweight property until it responds instead of racing OpenDoc6.
    import time

    last_error = None
    for _ in range(60):
        try:
            _ = app.RevisionNumber
            break
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(1)
    else:
        raise RuntimeError(f"SolidWorks did not become ready in time: {last_error}")

    app.Visible = True
    return app


def doc_type_for(path: Path) -> int:
    ext = path.suffix.lower()
    if ext == ".sldprt":
        return SW_DOC_PART
    if ext == ".sldasm":
        return SW_DOC_ASSEMBLY
    raise ValueError(f"unsupported CAD file type: {path.suffix}")


def _unwrap_model(result):
    # Early-bound (gencache) wrappers can flatten a method's [out] byref
    # parameters into a tuple alongside the primary return value; handle
    # both shapes defensively rather than assuming one.
    return result[0] if isinstance(result, tuple) else result


def export_stl(app, source: Path, dest: Path) -> None:
    # Under late binding, OpenDoc6's Errors/Warnings [out] params must be
    # passed as explicit ByRef VARIANTs, not plain Python ints.
    errors = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    warnings = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
    model = _unwrap_model(
        app.OpenDoc6(str(source), doc_type_for(source), 0, "", errors, warnings)
    )
    if model is None:
        raise RuntimeError(f"SolidWorks failed to open '{source}'")

    try:
        # OpenDoc6 already makes the newly opened document active; no
        # separate activation call needed for a single-document export.
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Plain SaveAs: simplest, most version-stable overload. Format is
        # inferred from the .stl extension; quality/binary-vs-ASCII follow
        # whatever this SolidWorks install's current export defaults are.
        ok = model.SaveAs(str(dest))
        if not ok:
            raise RuntimeError(f"SaveAs failed while exporting '{source}' to STL")
    finally:
        app.CloseDoc(model.GetTitle)


def run_smoke_test() -> int:
    if not SAMPLE_PART.is_file():
        print(f"Sample part not found: {SAMPLE_PART}", file=sys.stderr)
        return 1

    # Copy into a writable directory first: SolidWorks typically needs to
    # write a lock file next to an open document, which silently fails
    # under the read-only Program Files tree the sample ships in.
    work_dir = Path("scripts/_smoke_test_output")
    work_dir.mkdir(parents=True, exist_ok=True)
    source = work_dir / SAMPLE_PART.name
    shutil.copyfile(SAMPLE_PART, source)

    dest = work_dir / "sphere.stl"
    print(f"Connecting to SolidWorks...")
    app = connect()
    print(f"Exporting sample part '{source}' -> '{dest}'...")
    export_stl(app, source, dest)

    if not dest.is_file():
        print("Export reported success but output file is missing", file=sys.stderr)
        return 1

    print(f"OK: exported {dest.stat().st_size} bytes")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--smoke-test",
        action="store_true",
        help="Export a bundled SolidWorks sample part instead of scanning the project",
    )
    parser.add_argument(
        "source",
        nargs="?",
        default="03_SolidWorks_Project",
        help="Directory to scan for .SLDPRT/.SLDASM files",
    )
    parser.add_argument(
        "output",
        nargs="?",
        default="instructions/docs/assets/stls",
        help="Directory to write exported .stl files into",
    )
    args = parser.parse_args()

    if args.smoke_test:
        return run_smoke_test()

    source_dir = Path(args.source)
    output_dir = Path(args.output)
    if not source_dir.is_dir():
        print(f"Error: '{source_dir}' is not a directory", file=sys.stderr)
        return 1

    cad_files = sorted(
        p for p in source_dir.rglob("*") if p.suffix.lower() in (".sldprt", ".sldasm")
    )
    if not cad_files:
        print(f"No .SLDPRT/.SLDASM files found under '{source_dir}'")
        return 0

    app = connect()
    failures = 0
    for path in cad_files:
        dest = output_dir / (path.stem + ".stl")
        print(f"{path.name} -> {dest}")
        try:
            export_stl(app, path, dest)
        except Exception as exc:  # noqa: BLE001
            print(f"  FAILED: {exc}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
