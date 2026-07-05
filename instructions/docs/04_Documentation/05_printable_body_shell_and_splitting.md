# 05 - Printable Body Shell and Part Splitting

## Purpose

A 1:10 car body is often too large for a normal desktop printer. Even if it fits, printing it as one piece can create poor surface quality, too much support material, warping, and difficult post-processing.

Design the body as multiple printable parts from the beginning.

## Recommended body shell thickness

For FDM printing, start with:

```text
Body shell wall thickness: 1.6-2.4 mm
Large flat panel minimum: 2.0 mm or reinforced
Small cosmetic detail: >= 0.8-1.0 mm
Wheel arch lip: 1.2-2.0 mm
Mounting flange: 2.0-3.0 mm
```

These values are starting points. They depend on printer, nozzle size, material, orientation, and post-processing.

## Split strategy

Split along natural vehicle boundaries:

- front bumper,
- rear bumper,
- hood/bonnet line,
- trunk line,
- side skirt,
- wheel arch inside surfaces,
- roof-to-body joint if needed,
- door panel lines if appropriate.

Recommended printable body modules:

```text
Body_Shell_Cabin
Body_Front_Bumper
Body_Rear_Bumper
Body_Left_Side
Body_Right_Side
Body_Hood
Body_Trunk
Body_Left_Fender
Body_Right_Fender
```

For a simpler static model:

```text
Main_Body_Left
Main_Body_Right
Front_Bumper
Rear_Bumper
Hood
Trunk
```

## How to split in SolidWorks

Possible tools:

- `Split`,
- `Cut with Surface`,
- `Intersect`,
- `Save Bodies`,
- `Insert into New Part`,
- `Derived Part`,
- `Assembly > Insert Components`.

Basic workflow:

1. Create the complete body shell.
2. Create split surfaces or split planes.
3. Use `Split` to divide the solid body.
4. Rename resulting bodies clearly.
5. Use `Save Bodies` to export each as a separate part.
6. Create an assembly from saved bodies.
7. Add connectors and mounting features to each part.

## Hidden joint design

Use hidden joints to keep the outer surface clean.

Good joint locations:

- behind bumper edges,
- under side skirts,
- inside wheel arches,
- below the floor line,
- along existing panel gaps,
- under hood or trunk cut lines.

!!! warning "Bad joint locations"
    - middle of the roof,
    - middle of the door skin,
    - center of the bonnet,
    - highly visible curved exterior surfaces.

## Alignment features

Add features that make assembly repeatable.

Useful options:

```text
Alignment pins
Pin holes
Lap joints
Dovetail slides
Internal brackets
Screw bosses
Magnet pockets
Adhesive flanges
```

## Example lap joint

A simple lap joint can be used between two body sections.

Starting values:

```text
Overlap length: 6-12 mm
Clearance: 0.2-0.4 mm
Flange thickness: 1.5-2.5 mm
Screw boss nearby if removable
```

## Example pin joint

Starting values:

```text
Pin diameter: 3.0 mm
Hole diameter for FDM: 3.2-3.4 mm
Pin length: 5-8 mm
Chamfer: 0.3-0.5 mm
```

## Support-aware splitting

Before finalizing split lines, imagine how each part will sit in the slicer.

Prefer:

- visible exterior surfaces facing upward or outward,
- support material on hidden inner surfaces,
- smaller sections with stable bed contact,
- split bumper corners if support damage would be severe.

Avoid:

- large unsupported roof surfaces,
- exterior surface sitting directly on supports,
- tall unstable body sections,
- thin unsupported pillars.

## Body posts and chassis mounting

If the body attaches to a chassis, design mounting points early.

Options:

```text
Vertical body posts
Hidden screw mounts
Magnet mounts
Side clips
Internal chassis brackets
```

For static display, magnets or screws from underneath are clean.

For RC use, body posts are practical but less realistic visually.
