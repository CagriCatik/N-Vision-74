# 01 - Project Goal and 1:10 Scale Strategy

## Purpose

The purpose of this project is to design a 1:10 scale car in SolidWorks from blueprint images and prepare it for 3D printing.

This is different from a normal car surfacing exercise. A visual-only model can use open surfaces, very thin details, impossible joints, and one-piece geometry. A printable model must be designed with physical manufacturing constraints.

The final output should be:

- correctly scaled,
- solid and watertight where required,
- split into printable sections,
- assembled with tolerances,
- exportable as STL, 3MF, or STEP,
- validated through small test prints before full printing.

## Define the model type

Decide this before CAD work starts.

### Static display model

Use this if the vehicle is mainly for visual display.

Design focus:

- accurate exterior body,
- simple chassis plate,
- rolling or fixed wheels,
- separated mirrors, lights, grille, and bumpers,
- easy painting and assembly.

### Functional RC model

Use this if the car must drive.

Additional design focus:

- suspension mounting,
- steering angle,
- battery tray,
- servo mount,
- ESC and receiver space,
- motor mount,
- wheel hub and bearing geometry,
- screw access,
- chassis stiffness,
- replaceable crash parts.

## Scale calculation

Use this formula:

```text
CAD dimension = real vehicle dimension / 10
```

Example:

```text
Real car length: 4500 mm
1:10 CAD length: 450 mm
```

The most reliable scale references are:

1. wheelbase,
2. overall length,
3. overall width,
4. overall height,
5. wheel/tire diameter.

!!! tip
    Use wheelbase as the primary scaling reference if the blueprint image is slightly distorted.

## Printer-size check

Before modelling the body as one large part, compare the expected 1:10 dimensions with your printer build volume.

Example:

```text
Model length: 450 mm
Printer bed: 256 x 256 x 256 mm
Result: full body cannot be printed as one part.
```

!!! warning
    In that case, design split lines from the beginning.

## Recommended SolidWorks unit settings

Use:

```text
Unit system: MMGS
Length unit: millimetres
Angle unit: degrees
Mass unit: grams or kilograms
```

Keep all blueprint scaling, wall thickness, tolerance, and export settings in millimetres.

## Deliverables

Expected final CAD deliverables:

```text
Vehicle_1_10_Master.SLDASM
Body shell parts
Chassis parts
Wheel and tire parts
Mounting parts
STL or 3MF export files
Test-print notes
Assembly notes
```
