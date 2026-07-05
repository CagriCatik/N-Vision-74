# 04 - Body Surface Modelling Workflow in SolidWorks

## Why use surfacing?

Car bodies contain organic, blended, non-prismatic geometry. For this reason, surface modelling is usually more suitable than simple extrudes and cuts.

Typical SolidWorks tools for this stage:

- 3D Sketch,
- Project Curve,
- Split Line,
- Lofted Surface,
- Boundary Surface,
- Filled Surface,
- Sweep Surface,
- Trim Surface,
- Knit Surface,
- Thicken,
- Mirror,
- Zebra Stripes,
- Curvature Combs.

## Recommended modelling order

Do not start with details. Create the large body shape first.

```text
1. Side silhouette
2. Top-view width profile
3. Front and rear cross-sections
4. Roof, bonnet, trunk, and beltline curves
5. Wheel arch curves
6. Main body surfaces
7. Fender surfaces
8. Bumper surfaces
9. Door and panel lines
10. Shell thickness
11. Split for printing
12. Small details
```

## Step 1: Create main silhouette curves

Create separate sketches for:

```text
SK_Side_Roofline
SK_Side_Bonnet_Line
SK_Side_Beltline
SK_Side_Side_Skirt
SK_Side_Wheel_Arches
```

Use splines, but keep them clean.

Best practice:

- use fewer spline points,
- avoid many tiny segments,
- use tangent handles,
- inspect curvature combs,
- avoid sharp unintended curvature changes.

## Step 2: Create top-view width curves

Create curves for:

```text
SK_Top_Centerline
SK_Top_Left_Body_Outer_Profile
SK_Top_Right_Body_Outer_Profile
SK_Top_Bonnet_Width
SK_Top_Roof_Width
SK_Top_Rear_Width
```

If the vehicle is symmetrical, model one half and mirror later.

## Step 3: Create cross-sections

Create section sketches at important positions:

```text
Section_01_Front_Bumper
Section_02_Front_Wheel_Center
Section_03_A_Pillar
Section_04_B_Pillar
Section_05_C_Pillar
Section_06_Rear_Wheel_Center
Section_07_Rear_Bumper
```

Each section should define local width, height, and curvature.

## Step 4: Create guide curves

Guide curves control how surfaces flow between profiles.

Important guide curves:

```text
GC_Roof_Center
GC_Roof_Side
GC_Bonnet_Center
GC_Beltline
GC_Door_Lower_Line
GC_Fender_Top
GC_Side_Skirt
GC_Rear_Shoulder
```

SolidWorks recommends that guide curves should intersect all profiles when used with lofts. If a guide curve misses a profile, lofts often fail or twist.

## Step 5: Use Lofted Surface or Boundary Surface

### Lofted Surface

Use when you have ordered profiles from front to rear and one or more guide curves.

Typical use:

- roof surface,
- bonnet surface,
- side body panel,
- rear deck.

### Boundary Surface

Use when you need more control in two directions. Boundary Surface is often useful for complex car panels, fenders, and transitions because it can use curves in Direction 1 and Direction 2.

Typical use:

- fender transitions,
- bumper corners,
- hood-to-side transitions,
- rear quarter panel,
- roof-to-pillar transitions.

## Step 6: Work in patches

Do not try to create the whole body with one surface.

Recommended patch structure:

```text
Roof surface
Bonnet surface
Trunk surface
Left side panel
Right side panel
Front bumper
Rear bumper
Left fender surfaces
Right fender surfaces
Wheel arch lips
Side skirt surfaces
```

Patch-based modelling is easier to repair and easier to split for printing.

## Step 7: Knit surfaces

After surfaces are created:

1. Use `Knit Surface`.
2. Select adjacent surfaces.
3. Enable gap control if needed.
4. Try to form a closed surface body.
5. Use `Try to form solid` only when the surface body is closed.

If Knit fails, inspect open edges.

## Step 8: Use Thicken for printable shell

Once the outer body surface is acceptable:

1. Select the knitted surface.
2. Use `Thicken`.
3. Use inward thickening if the outer surface must keep exact dimensions.
4. Start with 1.6 mm to 2.4 mm for FDM body shell walls.
5. Check that tight corners do not self-intersect.

## Step 9: Add panel lines carefully

Panel lines can be created using:

- Split Line,
- shallow Cut-Extrude,
- projected sketches,
- engraved grooves,
- separate body panels.

For 3D printing, avoid extremely thin panel grooves. A groove that looks good on screen may disappear after printing, sanding, and painting.

Starting values:

```text
Panel groove width: 0.5-0.8 mm
Panel groove depth: 0.3-0.6 mm
Door gap visual line: 0.6-1.0 mm
```

## Step 10: Validate surface quality

Use:

- Zebra Stripes,
- Curvature Combs,
- Section View,
- Deviation Analysis if available.

Look for:

- surface waves,
- dents,
- twisted lofts,
- sharp unintended transitions,
- discontinuities between panels.

## Practical rule

If the surface looks wrong in zebra stripes, it will look worse after printing, sanding, and painting.
