# Online Resources and Best Practices

This chapter lists useful online references for SolidWorks blueprint setup, surface modelling, 3D printing export, and FDM design constraints.

## SolidWorks blueprint and Sketch Picture

### SolidWorks Web Help - Inserting and Resizing Sketch Pictures

URL: https://help.solidworks.com/2018/English/SolidWorks/sldworks/t_insert_and_resize_pictures.htm

Use this to understand how SolidWorks inserts sketch pictures and how the scale tool is used to resize a reference image.

Relevant use in this project:

- inserting side, top, front, and rear car blueprint views,
- scaling a blueprint to a known wheelbase,
- positioning images before tracing.

### YouTube - How To Insert Scaled Blueprint Images In Solidworks

URL: https://www.youtube.com/watch?v=T0ISIMIB2Xk

Useful for seeing the image import, scale, and transparency workflow visually.

### YouTube - How to Import and Trace an Image in SOLIDWORKS

URL: https://www.youtube.com/watch?v=ILormJ4H0jQ

Useful for learning how to import, scale, and trace image references in SolidWorks.

## SolidWorks surfacing and car body modelling

### SolidWorks Web Help - Recommendations for Lofts with Guide Curves

URL: https://help.solidworks.com/2021/English/SolidWorks/sldworks/c_Recommendations_Lofts_Guide_Curves.htm

Important point:

- guide curves should intersect all profiles when used with lofts.

Relevant use in this project:

- roof lofts,
- bonnet/hood lofts,
- fender surfaces,
- side panels,
- bumper transitions.

### MLC CAD - Complete SOLIDWORKS Surfacing Tutorial

URL: https://www.mlc-cad.com/resources/solidworks/complete-solidworks-surfacing-tutorial-step-by-step-guide/

Useful for understanding general surface creation, trimming, knitting, and turning surfaces into solids.

### Engineers Rule - The SOLIDWORKS Boundary Surface Feature

URL: https://www.engineersrule.com/the-solidworks-boundary-surface-feature/

Useful for understanding when Boundary Surface may be more flexible than Lofted Surface for complex patches.

### Hawk Ridge Systems - 3 Steps to Better Lofts and Boundaries in SOLIDWORKS

URL: https://hawkridgesys.com/blog/3-steps-better-lofts-boundaries-solidworks

Useful for avoiding bad loft or boundary surface geometry.

### YouTube - Design a Car in SOLIDWORKS Step-by-Step Surface Tutorial

URL: https://www.youtube.com/watch?v=yxeJnAEIS_w

Useful as a practical car-body surfacing reference.

### YouTube - Loft Surface in SolidWorks

URL: https://www.youtube.com/watch?v=PS3Yp9uwK2w

Useful for a short visual example of loft surfaces and guide curves.

## SolidWorks and 3D printing export

### SolidWorks Web Help - Exporting 3D Print Files

URL: https://help.solidworks.com/2025/English/SolidWorks/sldworks/t_exporting_3D_print_files.htm

Useful for understanding STL and 3MF export options. SolidWorks describes STL as triangulated surface geometry and 3MF as an additive manufacturing-focused format.

### MySolidWorks - STL Files

URL: https://my.solidworks.com/reader/onlinehelp/2021%252Fenglish%252Fsolidworks%252Fsldworks%252Fc_stl_files.htm/stl-files-stl

Useful for understanding STL/3MF/AMF export options.

### The SolidWorks Expert - Optimize SolidWorks Models for 3D Printing

URL: https://www.thesolidworksexpert.com/post/how-to-optimize-your-solidworks-models-for-3d-printing

Useful for practical SolidWorks-to-print preparation, including export and model checks.

### YouTube - How to Export STL Files in SolidWorks

URL: https://www.youtube.com/watch?v=b6VONCqFIgY

Useful for understanding STL export settings visually.

## FDM 3D printing design guidelines

### Forge Labs - FDM Design Guidelines

URL: https://forgelabs.com/design-guides/fdm

Useful for design considerations including wall thickness, overhangs, layer orientation, support strategy, and dimensional tolerances.

### 3D Demand - Design Guidelines for FDM 3D Printing

URL: https://www.3d-demand.com/blog/design-guidelines-for-fdm-3d-printing-wall-thickness-tolerances-file-prep

Useful for practical design constraints such as wall thickness, tolerances, overhangs, bridging, hole sizes, and file preparation.

### Stratasys Direct - FDM Material Tolerance Guide

URL: https://www.stratasys.com/en/stratasysdirect/resources/resource-guides/fdm-material-tolerance/

Useful for understanding how material and layer thickness influence FDM tolerance.

## Existing RC and 3D-printed vehicle references

### SolidWorks Blog - Design and Create a Remote Control Car

URL: https://blogs.solidworks.com/products/solidworks/solidworks-for-makers-design-and-create-a-remote-control-car-part-1/

Useful for maker-focused RC car design using SolidWorks.

### Instructables - 3D Printed RC Car

URL: https://www.instructables.com/3D-Printed-RC-Car/

Useful for practical assembly and printed vehicle design considerations.

### GitHub - 3D-Printed-RC-Car-Design

URL: https://github.com/Ahm3d0x/3D-Printed-RC-Car-Design

Useful as an example of a complete 3D-printed RC car design project.

### GrabCAD - SolidWorks car models

URL: https://grabcad.com/library/software/solidworks/tag/car

Useful for studying CAD structure and modelling approaches. Do not treat downloaded files as automatically printable; inspect them first.

## Practical learning path

1. Watch one Sketch Picture scaling tutorial.
2. Import and scale your own blueprint.
3. Build the master layout.
4. Study Loft and Boundary Surface examples.
5. Create only the roof, bonnet, and one side surface first.
6. Test `Knit Surface` and `Thicken` early.
7. Split one test body section and export it.
8. Print a small wheel arch or bumper section before modelling every detail.

## Bambu Lab printer and material resources

- Bambu Lab A1 mini technical specifications: build volume 180 x 180 x 180 mm.  
  https://bambulab.com/en/a1-mini/tech-specs

- Bambu Lab P1S product/spec information: enclosed printer, useful for ABS and other higher-temperature materials.  
  https://eu.store.bambulab.com/products/p1s

- Bambu Lab filament guide: printer, nozzle, build plate, compatibility and material guidance.  
  https://wiki.bambulab.com/en/general/filament-guide-material-table

- Bambu Lab PLA guide: includes PLA-specific operation notes and chamber-temperature related clogging risk.  
  https://wiki.bambulab.com/en/filament/pla

## How these resources affect this project

- The A1 mini build volume limits body modules to 180 x 180 x 180 mm if the part should be printable on both printers.
- The P1S build volume allows larger body sections and should be the main printer for the 1:10 body shell.
- PLA is the preferred first-iteration material.
- ABS should be reserved for P1S prints and structural or heat-exposed components.
- ABS requires more conservative part splitting, larger tolerances, and better anti-warping design than PLA.
