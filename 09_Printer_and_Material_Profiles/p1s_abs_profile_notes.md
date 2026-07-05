# P1S ABS Profile Notes

## Use case

Use this profile for functional chassis parts, brackets, body mounts, bumper mounts, motor/electronics areas, and final parts that need better heat resistance than PLA.

## CAD assumptions

| Parameter | Starting value |
|---|---:|
| Body wall thickness | 2.0-2.4 mm |
| Structural wall thickness | 2.4-4.0 mm |
| Assembly clearance | 0.35-0.60 mm |
| Pin/hole clearance | 0.30-0.50 mm |
| Internal fillet radius | 1.5-3.0 mm |
| Screw boss outer diameter | screw diameter x 3.0 |

## Slicer notes

```text
Printer: Bambu Lab P1S
Material: ABS
Layer height: 0.16-0.20 mm
Walls: 4-5
Infill body shell: 15-25%
Infill structural parts: 40-70%
Brim: recommended for large or flat parts
Enclosure: closed
```

## Design warnings

- ABS shrinks more than PLA. Do not reuse PLA clearance values without testing.
- Avoid large, flat, unreinforced plates.
- Split long body panels into smaller parts if warping appears.
- Use ribs and flanges to stiffen panels.
