# Printer and Material Decision Checklist

## Printer selection

- [ ] Does the part fit inside P1S build volume: 256 x 256 x 256 mm?
- [ ] Does the part fit inside A1 mini build volume: 180 x 180 x 180 mm?
- [ ] Is the part too large and does it need split lines?
- [ ] Are split lines hidden under panel gaps, bumpers, side skirts, or wheel arches?
- [ ] Is the selected print orientation already checked in the slicer?
- [ ] Are visible surfaces protected from support scars?

## PLA decision

Use PLA when:

- [ ] The part is a first prototype.
- [ ] The part is mainly visual.
- [ ] The part is not exposed to heat.
- [ ] The part is not a highly loaded RC component.
- [ ] Dimensional stability and easy printing matter more than heat resistance.

CAD checks for PLA:

- [ ] Wall thickness is at least 1.6-2.0 mm for body parts.
- [ ] Clearances are around 0.25-0.40 mm for assembly parts.
- [ ] Large flat panels have ribs, lips, or curvature.
- [ ] P1S chamber heat risk is considered for long PLA prints.

## ABS decision

Use ABS when:

- [ ] The part is structural.
- [ ] The part is a chassis, bracket, or mount.
- [ ] The part may be exposed to heat.
- [ ] The part needs better toughness than PLA.
- [ ] The part will be printed on the P1S, not the A1 mini.

CAD checks for ABS:

- [ ] Wall thickness is increased compared with PLA.
- [ ] Assembly clearance is increased to around 0.35-0.60 mm.
- [ ] Long flat panels are avoided or reinforced.
- [ ] Internal corners have fillets.
- [ ] Brim and enclosure strategy are planned.
- [ ] ABS-specific tolerance coupons are printed before final parts.

## SolidWorks-specific checks

- [ ] Printer build-volume reference boxes are inserted in the assembly.
- [ ] Each printable body module has been checked against the correct printer box.
- [ ] PLA and ABS configurations are separated where needed.
- [ ] Save Bodies exports are named by printer and material.
- [ ] STL/3MF export scale is verified in Bambu Studio.
- [ ] Part revision is included in the filename.

## Recommended filename convention

```text
PartName_Printer_Material_Revision.extension
```

Examples:

```text
Front_Bumper_P1S_PLA_R01.3mf
Chassis_Main_P1S_ABS_R03.3mf
Mirror_Left_A1Mini_PLA_R02.3mf
Tolerance_Coupon_P1S_ABS_R01.3mf
```
