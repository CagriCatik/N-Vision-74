# P1S PLA Profile Notes

## Use case

Use this profile for large body prototypes, final display body panels, roof/cabin sections, bumpers, and visible shell parts.

## CAD assumptions

| Parameter | Starting value |
|---|---:|
| Wall thickness | 1.8-2.2 mm |
| Assembly clearance | 0.25-0.40 mm |
| Pin/hole clearance | 0.20-0.35 mm |
| Minimum visible detail | 0.8-1.0 mm |
| Screw boss outer diameter | screw diameter x 2.5-3.0 |

## Slicer notes

```text
Printer: Bambu Lab P1S
Material: PLA
Layer height: 0.16-0.20 mm
Walls: 3-4
Infill body shell: 10-20%
Supports: minimize on visible surfaces
Seam: place on underside, inner edge, or panel line
```

## Design warnings

- Do not overheat PLA in the enclosed chamber.
- For long PLA prints, follow Bambu Studio/Bambu Lab recommendations for top cover or door position.
- Avoid very thin large panels; use internal lips or ribs.
