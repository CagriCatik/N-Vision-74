# 08 - Export, Slicing, and Print Iteration

## Before export

Check each part before exporting:

- solid body, not only open surfaces,
- no missing faces,
- no self-intersections,
- correct scale in millimetres,
- correct body orientation,
- wall thickness suitable for printing,
- assembly clearance included,
- file name includes revision.

## SolidWorks checks

Use:

- `Evaluate > Check`,
- `Evaluate > Interference Detection`,
- `Evaluate > Measure`,
- `Section View`,
- `Mass Properties`,
- `Import Diagnostics` if imported geometry is used.

## Export formats

### STL

Most common format for slicers. STL stores triangulated surface geometry only. It does not preserve feature history, colours, or parametric data.

### 3MF

Useful for additive manufacturing workflows. SolidWorks documentation describes 3MF as an additive manufacturing-focused format for sending full-fidelity 3D models to other applications, platforms, services, and printers.

### STEP

Useful for sharing clean CAD geometry or sending to services that can process CAD files directly. STEP is not usually sliced directly in basic slicers, but it is good for manufacturing exchange.

## Recommended export workflow

1. Save the SolidWorks part.
2. Suppress unnecessary reference sketches and images if they affect export.
3. Export as 3MF if your slicer supports it.
4. Export as STL for broad compatibility.
5. Open exported file in slicer.
6. Confirm dimensions with slicer measurement tools.
7. Check support requirements.
8. Save slicer project with settings.

## STL resolution

Avoid very coarse STL resolution because car body surfaces will look faceted.

Use fine or custom export settings. However, do not create unnecessarily huge files.

Check curved surfaces such as:

- roof,
- bonnet,
- fenders,
- wheel arches,
- bumpers.

If curves look polygonal in the slicer, increase export resolution.

## Slicer orientation strategy

For body parts:

- protect visible exterior surfaces,
- place supports on hidden inner surfaces where possible,
- split parts if support scars would appear on visible surfaces,
- avoid tall unstable prints,
- add brims for long thin body sections if needed.

For chassis parts:

- orient for strength,
- keep screw bosses strong,
- reduce support inside screw holes,
- avoid layer separation in loaded brackets.

## Test-print plan

Do not print the full car first.

Print in this order:

```text
1. Clearance and tolerance coupon
2. Screw boss sample
3. Alignment pin sample
4. Wheel/tire sample
5. Wheel arch section
6. Body split joint sample
7. Small bumper section
8. Chassis corner sample
9. One full body section
10. Full vehicle print
```

## Iteration log

Record every print iteration.

Use this format:

```text
Iteration: R01
Part: Front bumper
Material: PLA
Nozzle: 0.4 mm
Layer height: 0.2 mm
Infill: 15%
Wall loops: 3
Issue: left joint too tight
Change for R02: increase clearance from 0.2 mm to 0.4 mm
```

Save photos and slicer screenshots in:

```text
08_Print_Iterations/
```
