# 03 - SolidWorks Master Layout Strategy

## Purpose of the master layout

The master layout controls the whole vehicle. It prevents the model from becoming visually correct but dimensionally inconsistent.

The master layout should define:

- scale,
- axle positions,
- overall size,
- centreline,
- body envelope,
- chassis envelope,
- ground clearance,
- split-line zones,
- main mounting points.

## Recommended file

Create:

```text
00_Master_Layout.SLDPRT
```

Use this as a reference part inside the final assembly.

## Master sketches

Create the following sketches:

```text
01_Global_Side_Layout
02_Global_Top_Layout
03_Global_Front_Layout
04_Axle_and_Wheel_Layout
05_Body_Split_Line_Layout
06_Chassis_Mounting_Layout
```

## Essential reference geometry

Create these planes and axes:

```text
Vehicle_Center_Plane
Ground_Plane
Front_Axle_Plane
Rear_Axle_Plane
Front_Bumper_Limit_Plane
Rear_Bumper_Limit_Plane
Roof_Height_Plane
Max_Width_Left_Plane
Max_Width_Right_Plane
```

## Suggested dimension variables

Use global variables in SolidWorks equations where possible.

Example:

```text
Scale = 0.1
Real_Wheelbase = 2700mm
Model_Wheelbase = Real_Wheelbase * Scale
Real_Length = 4500mm
Model_Length = Real_Length * Scale
Body_Wall = 2.0mm
Assembly_Clearance = 0.3mm
```

## How to use equations

1. Go to `Tools > Equations`.
2. Create global variables.
3. Use these variables in sketches and features.
4. Avoid hardcoding repeated values.

This makes the model easier to update if the scale, wall thickness, or assembly clearance changes.

## Layout-driven modelling approach

Use this workflow:

```text
Master layout controls important dimensions
↓
Individual part files reference layout dimensions
↓
Assembly checks fit and interference
↓
Exported print parts remain consistent
```

## Do not overconstrain blueprint traces

When tracing over images, keep curves flexible. Use dimensions only where they matter:

- wheelbase,
- overall length,
- width,
- height,
- axle locations,
- wheel diameter,
- mounting positions.

Do not fully constrain every artistic spline. Overconstrained splines become hard to adjust.

## Recommended sketch naming

Use meaningful names:

```text
SK_Side_Roofline
SK_Side_Beltline
SK_Top_Body_Width
SK_Front_Cross_Section
SK_Rear_Cross_Section
SK_Wheel_Arches
SK_Split_Lines
```

This matters later because car-body surfacing can create many sketches and reference curves.
