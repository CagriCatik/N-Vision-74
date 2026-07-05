# 02 - Blueprint Preparation and Import into SolidWorks

## Required blueprint views

Use at least four views:

- side view,
- top view,
- front view,
- rear view.

Optional but useful:

- wheel detail,
- interior view,
- chassis underside,
- headlight close-up,
- grille close-up.

## Prepare the images before importing

Before inserting images into SolidWorks:

1. Crop each view separately.
2. Align each view horizontally or vertically.
3. Remove unnecessary background.
4. Keep the same resolution ratio where possible.
5. Save each view as a separate PNG or JPG.

Recommended names:

```text
side_view.png
top_view.png
front_view.png
rear_view.png
```

Place them into:

```text
01_Blueprints/
```

## Import using Sketch Picture

SolidWorks uses `Sketch Picture` to insert reference images into sketches. The image can be resized using the built-in scale tool. SolidWorks documentation states that inserting a picture displays the scale tool automatically and that it can be resized by dragging handles or using the scale tool.

### Side view setup

1. Open `00_Master_Layout.SLDPRT`.
2. Select the `Right Plane`.
3. Start a new sketch.
4. Go to `Tools > Sketch Tools > Sketch Picture`.
5. Insert `side_view.png`.
6. Use the scale tool to match the known 1:10 wheelbase.
7. Move the image so the rear axle or vehicle centreline is close to the origin.
8. Set transparency so sketch curves remain visible.
9. Lock the sketch picture position after scaling.

### Top view setup

1. Select the `Top Plane`.
2. Insert `top_view.png` as a Sketch Picture.
3. Scale using overall length or wheelbase.
4. Align the car centreline with the SolidWorks origin line.
5. Match the front and rear axle positions with the side view.

### Front and rear view setup

1. Select the `Front Plane`.
2. Insert `front_view.png`.
3. Scale by overall width or height.
4. Align the center of the car to the vertical origin line.
5. Use separate offset planes if front and rear images overlap visually.

## Critical alignment points

Always align these across all views:

- front wheel centre,
- rear wheel centre,
- ground line,
- vehicle centreline,
- roof height,
- front bumper end,
- rear bumper end,
- maximum body width.

## Avoid direct blind tracing

Blueprints from the internet are often inaccurate. Do not trace every line blindly.

Instead:

- trace only major silhouette curves,
- create clean SolidWorks splines,
- use real dimensions to correct proportions,
- rebuild surfaces using controlled curves.

## Practical SolidWorks tips

### Use construction geometry

Convert blueprint reference lines to construction geometry. Do not use them directly as production geometry.

### Use separate sketches

Avoid putting all curves into one sketch. Use separate sketches for:

```text
Side_Profile_Sketch
Top_Profile_Sketch
Front_Sections_Sketch
Rear_Sections_Sketch
Wheelbase_Reference_Sketch
```

### Use display states or hide/show folders

Keep blueprint images and construction sketches in folders so they can be hidden during later modelling.

## Quality check before continuing

Before body modelling, verify:

- side view wheelbase matches the scaled value,
- top view length matches the side view,
- front view width matches the top view,
- roof height matches side and front views,
- axle positions are consistent.
