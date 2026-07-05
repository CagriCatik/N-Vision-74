# 10 - Bambu Lab P1S, A1 mini, PLA and ABS Material Strategy

## Purpose of this chapter

This chapter adapts the 1:10 SolidWorks car workflow to the available printers and filaments:

- Bambu Lab P1S
- Bambu Lab A1 mini
- PLA filament
- ABS filament

The main design consequence is simple:

- use the P1S for larger body sections and ABS-capable parts,
- use the A1 mini mainly for small PLA parts, test coupons, details, jigs, wheels, mirrors, brackets, and prototypes,
- design body split lines around the smaller A1 mini build volume only if you want every part to be printable on both printers,
- avoid ABS on the A1 mini for large parts because it is an open-frame printer and ABS warping risk is high.

## Printer constraints

### Bambu Lab P1S

Relevant design facts:

- enclosed CoreXY FDM printer,
- build volume: 256 x 256 x 256 mm,
- suitable for larger body sections than the A1 mini,
- better choice for ABS because the enclosure helps reduce warping,
- useful for chassis, body panels, bumpers, and larger split sections.

For this 1:10 car project, the P1S should be the main printer.

### Bambu Lab A1 mini

Relevant design facts:

- open-frame bedslinger FDM printer,
- build volume: 180 x 180 x 180 mm,
- very useful for quick PLA prototypes and small parts,
- not ideal for large ABS parts because there is no enclosed chamber,
- good for detail pieces, test coupons, smaller wheels, mirrors, light housings, alignment pins, body clips, and tolerance samples.

For this 1:10 car project, the A1 mini should be treated as the prototyping and small-part printer.

## Build volume impact on a 1:10 car

A typical real vehicle may be around 4,300 to 4,800 mm long. At 1:10 scale, the model becomes approximately 430 to 480 mm long.

This means the full car body cannot be printed in one piece on either printer.

Approximate comparison:

| Item | Approximate size |
|---|---:|
| 1:10 car length | 430-480 mm |
| P1S build volume | 256 x 256 x 256 mm |
| A1 mini build volume | 180 x 180 x 180 mm |

Therefore, the body shell must be split.

## Recommended printer assignment

| Part type | Preferred printer | Preferred material | Reason |
|---|---|---|---|
| Large body side panels | P1S | PLA first, ABS later | Larger build volume and better thermal control |
| Roof/cabin section | P1S | PLA first, ABS later | Large visible part, needs stable print |
| Front bumper | P1S or A1 mini | PLA or ABS | Can be split if needed |
| Rear bumper | P1S or A1 mini | PLA or ABS | Can be split if needed |
| Chassis plate | P1S | ABS if functional, PLA if display | Chassis benefits from thermal resistance and toughness |
| Small brackets | A1 mini or P1S | PLA for prototypes, ABS for final | Small parts are easy to test |
| Mirrors | A1 mini | PLA | Small detail part |
| Headlight housings | A1 mini | PLA | Small and low-load |
| Wheel prototypes | A1 mini | PLA | Fast iteration |
| Functional wheel hubs | P1S | ABS or stronger material later | More load and heat resistance needed |
| Tolerance coupons | A1 mini | Same material as final part | Fast testing |

## PLA strategy

PLA is the easiest material for first iterations.

Use PLA for:

- blueprint proportion validation,
- body shape prototypes,
- fit checks,
- alignment pin tests,
- screw boss tests,
- visual body shell mockups,
- mirrors, lights, grilles, badges, and non-load details.

Advantages:

- easy to print,
- low warping,
- good surface quality,
- good for large visual prototypes,
- good dimensional consistency.

Limitations:

- lower heat resistance,
- can soften in hot environments,
- not ideal for car interior storage in summer,
- more brittle than ABS for impact-loaded RC parts.

### PLA design recommendations

For PLA body shell parts:

| Feature | Starting value |
|---|---:|
| Wall thickness | 1.6-2.0 mm |
| Wall loops | 3-4 |
| Layer height | 0.16-0.20 mm |
| Infill for body shell | 10-15% |
| Infill for brackets | 30-50% |
| Clearance for fitted parts | 0.25-0.40 mm |
| Pin/hole clearance | 0.20-0.35 mm |
| Minimum detail thickness | 0.8-1.0 mm |

### PLA printer choice

PLA can be printed on both P1S and A1 mini.

Use the A1 mini for:

- test coupons,
- small details,
- fit samples,
- wheel arch test sections,
- screw boss samples.

Use the P1S for:

- larger body panels,
- large roof sections,
- long bumper sections,
- large chassis prototypes.

!!! warning "Important note for PLA on enclosed printers"
    When printing PLA on the P1S, avoid excessive chamber heat. If the chamber becomes too warm, PLA can soften too early and cause extrusion or clogging issues. For long PLA prints, consider opening the top cover or door depending on the filament and Bambu Studio recommendation.

## ABS strategy

ABS is more suitable than PLA for some final functional parts, but it is more difficult to print.

Use ABS for:

- functional chassis parts,
- motor or electronics mounting areas,
- brackets exposed to heat,
- parts that need better impact resistance,
- parts that may be sanded, filled, primed, or acetone-smoothed.

Avoid ABS for:

- first body shape validation,
- very large thin panels without proper split strategy,
- A1 mini large parts,
- parts where warping would destroy the fit.

### ABS design recommendations

For ABS parts:

| Feature | Starting value |
|---|---:|
| Body wall thickness | 2.0-2.4 mm |
| Chassis/bracket wall thickness | 2.4-4.0 mm |
| Wall loops | 4-5 |
| Infill for body parts | 15-25% |
| Infill for chassis parts | 40-70% |
| Clearance for fitted parts | 0.35-0.60 mm |
| Pin/hole clearance | 0.30-0.50 mm |
| Brim | recommended for large flat parts |
| Internal fillets | strongly recommended |

!!! warning
    ABS shrinks more than PLA, so PLA-fit dimensions should not automatically be reused for ABS. Print separate ABS tolerance coupons.

### ABS printer choice

Use the P1S for ABS.

!!! warning
    Avoid large ABS prints on the A1 mini because the open frame makes warping more likely, especially for long body panels, chassis sections, and large flat parts.

## SolidWorks design rules based on your printers

## 1. Add printer-specific bounding boxes

Create two reference boxes in SolidWorks:

```text
P1S_Print_Volume = 256 x 256 x 256 mm
A1Mini_Print_Volume = 180 x 180 x 180 mm
```

Recommended method:

1. Create a new part called `Printer_Build_Volumes.SLDPRT`.
2. Create one transparent block for the P1S build volume.
3. Create one transparent block for the A1 mini build volume.
4. Insert this part into the main vehicle assembly.
5. Use it to check whether each split body section fits.

This prevents designing a beautiful part that cannot be printed on your machines.

## 2. Split the body for the P1S first

For a 1:10 vehicle, design the main body split around the P1S.

Possible body split:

```text
Body_Shell
├── Front_Body_Module
├── Cabin_Roof_Module
├── Rear_Body_Module
├── Left_Side_Sill
├── Right_Side_Sill
├── Front_Bumper
├── Rear_Bumper
├── Hood
└── Trunk
```

The exact split depends on the vehicle geometry, but each body module should fit inside 256 x 256 x 256 mm after orientation.

## 3. Add optional A1 mini split lines

If you want parts to be printable on both printers, create additional split configurations:

```text
Body_Shell_P1S_Split
Body_Shell_A1Mini_Split
```

In SolidWorks, this can be handled with:

- configurations,
- Split feature,
- derived parts,
- Save Bodies,
- separate export configurations.

The A1 mini split version will need more seams, more alignment pins, and more post-processing.

## 4. Use different configurations for PLA and ABS

Create material-specific configurations for important parts:

```text
Body_Shell_PLA_Prototype
Body_Shell_ABS_Final
Chassis_PLA_FitCheck
Chassis_ABS_Functional
```

Possible differences:

- ABS version has thicker walls,
- ABS version has larger clearances,
- ABS version has more ribs,
- ABS version has stronger screw bosses,
- ABS version has larger fillets,
- ABS version avoids very long flat panels.

## 5. Add shrinkage and tolerance notes directly in SolidWorks

Use custom properties or design notes:

```text
Material: PLA
Printer: Bambu Lab P1S
Clearance target: 0.30 mm
Wall thickness: 2.0 mm
Export format: 3MF + STL
Revision: R03
```

For ABS:

```text
Material: ABS
Printer: Bambu Lab P1S
Clearance target: 0.50 mm
Wall thickness: 2.4 mm
Brim: yes
Split line: hidden under side skirt
Revision: R02
```

## Body shell recommendations for your setup

### First prototype

Use PLA.

Recommended:

- printer: P1S for large sections, A1 mini for small samples,
- nozzle: 0.4 mm,
- layer height: 0.20 mm for rough shape, 0.16 mm for cleaner exterior,
- wall thickness in CAD: 1.8-2.0 mm,
- split into large but manageable modules,
- avoid tiny details during first body print.

Purpose:

- check proportions,
- check blueprint accuracy,
- check body-to-chassis fit,
- check wheel arch clearance,
- check assembly joints.

### Final display model

Use PLA if the model is mainly decorative and will stay indoors.

Recommended:

- printer: P1S for body, A1 mini for details,
- material: PLA,
- layer height: 0.12-0.16 mm for visible body panels,
- wall thickness: 1.8-2.2 mm,
- more separate detail parts for painting,
- sand, prime, paint after assembly.

### Final functional RC-style model

Use ABS for chassis and load-bearing parts. Use PLA only for low-load visual details unless heat exposure is not an issue.

Recommended:

- printer: P1S,
- material: ABS for chassis, brackets, body mounts,
- PLA or ABS for body shell depending on use,
- wall thickness: 2.0-2.4 mm for body, 2.4-4.0 mm for structural parts,
- large fillets on brackets,
- metal screws and shafts,
- brass heat-set inserts if possible,
- separate replaceable bumper mounts.

## Chassis recommendations for PLA vs ABS

### PLA chassis prototype

Use for:

- geometry validation,
- wheelbase check,
- body mounting check,
- electronics packaging mockup.

Avoid using PLA chassis as final if the vehicle is driven hard or exposed to heat.

### ABS chassis final

Use for:

- better impact resistance,
- better temperature resistance,
- stronger brackets,
- functional RC use.

Design changes for ABS chassis:

- thicker mounting tabs,
- ribs instead of solid blocks,
- large internal fillets,
- screw bosses with generous outer diameter,
- avoid long flat unreinforced plates,
- design removable front and rear crash structures.

## Recommended test coupons

Before printing the full vehicle, create these small SolidWorks test parts:

```text
Tolerance_Coupon_PLA_A1Mini.SLDPRT
Tolerance_Coupon_PLA_P1S.SLDPRT
Tolerance_Coupon_ABS_P1S.SLDPRT
Screw_Boss_Test_PLA.SLDPRT
Screw_Boss_Test_ABS.SLDPRT
Alignment_Pin_Test_PLA.SLDPRT
Alignment_Pin_Test_ABS.SLDPRT
Wall_Thickness_Surface_Test.SLDPRT
Wheel_Arch_Clearance_Test.SLDPRT
```

Each coupon should be saved with the slicer profile used.

## Recommended slicer profile logic

### PLA body prototype

Use when checking shape and assembly.

```text
Printer: P1S or A1 mini
Material: PLA
Layer height: 0.20 mm
Walls: 3
Infill: 10-15%
Supports: only where needed
Brim: only for narrow parts
```

### PLA visual final

Use when exterior quality matters.

```text
Printer: P1S
Material: PLA
Layer height: 0.12-0.16 mm
Walls: 3-4
Infill: 10-20%
Supports: carefully placed away from visible surfaces
Seam: hide on underside or panel line
```

### ABS functional final

Use when strength and heat resistance matter.

```text
Printer: P1S
Material: ABS
Layer height: 0.16-0.20 mm
Walls: 4-5
Infill: 40-70% for structural parts
Brim: recommended
Enclosure: closed
Cooling: conservative
Supports: avoid support scars on visible surfaces
```

## Practical decision rule

Use this rule during design:

```text
Is the part large and visible?
→ P1S, PLA first, maybe ABS later.

Is the part small and only for fit testing?
→ A1 mini, PLA.

Is the part structural or heat-exposed?
→ P1S, ABS.

Is the part a large thin ABS body panel?
→ Split it smaller, add ribs/flanges, print on P1S, use brim.

Does the part need to fit on both printers?
→ Design to 180 x 180 x 180 mm and accept more seams.
```

## Folder addition for printer profiles

Add this folder to the project:

```text
09_Printer_and_Material_Profiles/
├── p1s_pla_profile_notes.md
├── p1s_abs_profile_notes.md
├── a1mini_pla_profile_notes.md
└── tolerance_coupon_results.md
```

Store exported Bambu Studio projects or screenshots here if needed.

## Online references

- Bambu Lab A1 mini technical specifications: build volume 180 x 180 x 180 mm.
- Bambu Lab P1S product/spec references: enclosed printer, 256 x 256 x 256 mm build volume.
- Bambu Lab filament guide: material and printer compatibility guidance.
- Bambu Lab PLA guide: notes that excessive internal printer temperature can soften PLA and cause feeding/clogging issues.
- FDM design guides: wall thickness, tolerance, layer orientation, support strategy, and warping constraints.
