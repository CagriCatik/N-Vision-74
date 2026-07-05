# Parts Inventory

A comprehensive catalog of all N-Vision-74 components organized by assembly section.

## Master Assembly Structure

```
Vehicle_1_10_Master.SLDASM
├── 00_Master_Layout.SLDPRT
├── 01_Body_Shell_Main.SLDPRT
├── 02_Body_Front_Bumper.SLDPRT
├── 03_Body_Rear_Bumper.SLDPRT
├── 04_Chassis_Main_Plate.SLDPRT
├── 05_Chassis_Front_Module.SLDPRT
├── 06_Chassis_Rear_Module.SLDPRT
├── 07_Wheel.SLDPRT
├── 08_Tire.SLDPRT
├── 09_Mirror_Left.SLDPRT
├── 10_Mirror_Right.SLDPRT
├── 11_Light_Housings.SLDPRT
└── 12_Interior_Tub.SLDPRT
```

## Naming Convention

All parts follow a consistent naming pattern for easy identification and revision tracking.

### Standard Format
```
[Number]_[Component_Name].SLDPRT
[Number]_[Component_Name]_R[Revision].SLDPRT
```

### Examples
- `01_Body_Shell_Main.SLDPRT` - Initial release
- `01_Body_Shell_Main_R02.SLDPRT` - Revision 2
- `01_Body_Shell_Main_R02.stl` - STL export
- `01_Body_Shell_Main_R02.3mf` - 3MF export

## Body & Shell Assembly

### Main Components

| Part # | Name | Type | Material | Status |
|--------|------|------|----------|--------|
| 01 | Body Shell Main | Frame | Polycarbonate | Complete |
| 02 | Body Front Bumper | Bumper | TPU Plastic | Complete |
| 03 | Body Rear Bumper | Bumper | TPU Plastic | Complete |
| 11 | Light Housings | Accessory | Plastic | Complete |
| 12 | Interior Tub | Interior | Plastic | Complete |
| 09 | Mirror Left | Accessory | Plastic | Complete |
| 10 | Mirror Right | Accessory | Plastic | Complete |

## Chassis Assembly

| Part # | Name | Type | Material | Status |
|--------|------|------|----------|--------|
| 00 | Master Layout | Reference | Steel | Complete |
| 04 | Chassis Main Plate | Frame | Aluminum | Complete |
| 05 | Chassis Front Module | Suspension Mount | Aluminum | Complete |
| 06 | Chassis Rear Module | Suspension Mount | Aluminum | Complete |
| 07 | Wheel | Rolling | Aluminum | Complete |
| 08 | Tire | Rolling | Rubber | Complete |

## Suspension System

### Front Suspension

| Component | Revision | Material | Notes |
|-----------|----------|----------|-------|
| Front Tower Assembly | R01 | Aluminum | Main mount point |
| Front Arm Top (L/R) | R01 | Aluminum 7075 | High strength |
| Front Arm Bottom (L/R) | R01 | Aluminum 7075 | Compliant design |
| Front Arm Holder (Front) | R01 | Plastic | 3D printable |
| Front Arm Holder (Rear) | R01 | Plastic | 3D printable |
| Front Hub (L/R) | R01 | Aluminum | Wheel mount |
| Shock Adapter Set | R01 | Plastic | Various angles |

### Rear Suspension

| Component | Revision | Material | Notes |
|-----------|----------|----------|-------|
| Rear Tower Assembly | R01 | Aluminum | Main mount point |
| Rear Arm (L/R) | R01 | Aluminum 7075 | High strength |
| Rear Arm Holder (Front) | R01 | Plastic | 3D printable |
| Rear Arm Holder (Rear) | R01 | Plastic | 3D printable |
| Rear Hub (L/R) | R01 | Aluminum | Wheel mount |
| Shock Adapter Set | R01 | Plastic | Various angles |

## Drivetrain Assembly

| Component | Revision | Material | Status |
|-----------|----------|----------|--------|
| Center Differential Body | R01 | Aluminum | Complete |
| Center Diff Top | R01 | Plastic | Complete |
| Center Diff Bottom | R01 | Aluminum | Complete |
| Diff Top Cover | R01 | Plastic | Complete |
| Diff Sway Bar Cover | R01 | Plastic | Complete |
| Motor Support Mount (1-3) | R01 | Aluminum | Complete |
| Center Brace Holder | R01 | Aluminum | Complete |

## Electronics Mounting

| Component | Revision | Material | Notes |
|-----------|----------|----------|--------|
| Battery Tray (L/R) | R01 | Plastic | Modular mounting |
| ESC Box Body | R01 | Plastic | Waterproof |
| Electronics Cover | R01 | Plastic | Dust seal |
| Fan Shroud | R01 | Plastic | Motor cooling |
| On/Off Switch Holder | R01 | Plastic | Easy access |

## Steering System

| Component | Revision | Material | Status |
|-----------|----------|----------|--------|
| Steering System Assembly | R01 | Mixed | Complete |
| Left Steering Arm | R01 | Steel | M4 threaded |
| Right Tower Lower | R01 | Aluminum | Precision |
| Tie Rod Assemblies | R01 | Aluminum | Adjustable |

## Fastener Specifications

### Socket Head Cap Screws

| Size | Quantity | Material | Grade |
|------|----------|----------|-------|
| M3 x 6mm | 40 | Stainless Steel | A4 |
| M3 x 8mm | 30 | Stainless Steel | A4 |
| M3 x 10mm | 25 | Stainless Steel | A4 |
| M4 x 8mm | 20 | Stainless Steel | A4 |
| M4 x 10mm | 30 | Stainless Steel | A4 |
| M5 x 12mm | 15 | Stainless Steel | A4 |

### Nuts & Washers

| Type | Size | Quantity | Material |
|------|------|----------|----------|
| Flanged Nut | M3 | 50 | Stainless Steel |
| Flanged Nut | M4 | 40 | Stainless Steel |
| Lock Washer | M3 | 60 | Stainless Steel |
| Lock Washer | M4 | 50 | Stainless Steel |
| Spring Washer | M3 | 40 | Steel |
| Spring Washer | M4 | 30 | Steel |

## Assembly Sequence

### Recommended Build Order
1. **Chassis Assembly** - Build main platform
2. **Suspension Systems** - Front and rear
3. **Drivetrain** - Differential and motor mounts
4. **Steering** - Servo and linkages
5. **Electronics** - ESC, motor, battery mounting
6. **Body & Shell** - Final enclosure
7. **Accessories** - Mirrors, lights, decals

## Part Tracking

### Inventory Management Tips

- ✓ Check all parts against BOM before starting
- ✓ Organize by assembly section during assembly
- ✓ Label drawers/containers with part numbers
- ✓ Keep extra fasteners in a separate container
- ✓ Mark revisions on printed assemblies

### Revision Control

When ordering replacement parts:
- Always reference the **latest revision** number
- Check the **CAD files** for current specifications
- Compare part dimensions before substitution
- Document any modifications made

---

**Master Assembly Version:** 1.0  
**Last Updated:** 2026-07-05
