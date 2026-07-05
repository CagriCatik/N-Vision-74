# 1:10 Scale Calculation Template

Fill this table before starting the CAD model.

## Hyundai N Vision 74 — official dimensions

Read directly from the Hyundai Design Center blueprint sheet (`01_Blueprints/5K-Original.png`, dimension block and labeled callouts, drawn by Jisoo Kim, dated Feb 24 2022). Click the image to open it full-size and compare against the table below.

[![Hyundai N Vision 74 blueprint sheet — Top, Front, Side, and Rear views with dimension block](../01_Blueprints/5K-Black.png)](../01_Blueprints/5K-Black.png)

| Parameter | Real vehicle dimension | 1:10 model dimension | CAD reference used? |
|---|---:|---:|---|
| Overall length (excl. rear spoiler) | 4952 mm | 495.2 mm | 5K-Original.png, side view |
| Overall length (incl. rear spoiler) | 5085 mm | 508.5 mm | 5K-Original.png, top view |
| Overall width | 1995 mm | 199.5 mm | 5K-Original.png, top view |
| Overall height | 1331 mm | 133.1 mm | 5K-Original.png, side view |
| Wheelbase | 2905 mm | 290.5 mm | 5K-Original.png, top + side view |
| Front overhang (FOH) | 990 mm | 99.0 mm | Dimension block |
| Rear overhang (ROH) | 1050 mm | 105.0 mm | Dimension block |
| Front track width | not labeled on blueprint | — | not available |
| Rear track width | not labeled on blueprint | — | not available |
| Wheel outer diameter (front) | 700.5 mm | 70.05 mm | derived from tire code 275/35R20 |
| Wheel outer diameter (rear) | 728.4 mm | 72.84 mm | derived from tire code 325/30R21 |
| Tire width (front) | 275 mm | 27.5 mm | dimension block: F. Wheel 275/35R20 |
| Tire width (rear) | 325 mm | 32.5 mm | dimension block: R. Wheel 325/30R21 |
| Ground clearance | not specified on blueprint | — | not available |

!!! note "Front/rear track width and ground clearance"
    These are not labeled anywhere on the official blueprint or its dimension block. Do not guess a value — measure them directly from the top/front view drawing at full resolution if needed, or treat them as open items to confirm before finalizing the chassis width.

!!! tip "Wheel outer diameter formula"
    Tire size codes follow `[width]/[aspect ratio]R[rim diameter in inches]`. Outer diameter = rim diameter (in mm) + 2 × (width × aspect ratio / 100).

    ```text
    Front 275/35R20: 20 in = 508 mm rim
      sidewall height = 275 x 0.35 = 96.25 mm
      outer diameter = 508 + 2 x 96.25 = 700.5 mm

    Rear 325/30R21: 21 in = 533.4 mm rim
      sidewall height = 325 x 0.30 = 97.5 mm
      outer diameter = 533.4 + 2 x 97.5 = 728.4 mm
    ```

## Additional labeled dimensions (unconfirmed reference points)

The blueprint has a few more dimension lines that are visible but whose exact reference points are not fully certain without inspecting the full-resolution drawing directly in SolidWorks:

| Label on drawing | Value | Likely meaning |
|---|---:|---|
| Top view, secondary width line | 1630 mm | possibly front track width or cabin width — unconfirmed |
| Side view, front dimension | 780 mm | unconfirmed reference point |
| Side view, rear dimension | 520 mm | possibly rear deck/spoiler height reference — unconfirmed |

!!! warning
    Verify these three against the blueprint directly before using them as scaling references. They are included here for completeness, not as confirmed CAD inputs.

## Blank template for other measurements

Use this table for any additional parameters not covered above, or when working from a different reference source.

| Parameter | Real vehicle dimension | 1:10 model dimension | CAD reference used? |
|---|---:|---:|---|
|  |  |  |  |

Formula:

```text
1:10 model dimension = real dimension / 10
```

Example:

```text
Real wheelbase: 2700 mm
1:10 CAD wheelbase: 270 mm
```

!!! tip
    Use the wheelbase as the primary scaling reference if the blueprint image is distorted. Use overall length and height as secondary checks.
