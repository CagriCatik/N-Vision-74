# Recommended SolidWorks File Plan

Use an assembly-driven structure instead of modelling the whole vehicle as one part.

```text
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

## Naming rules

- Use clear part names.
- Avoid `Part1`, `Body_final_final`, or uncontrolled duplicates.
- Add revision suffixes only when needed, for example `Body_Shell_Main_R02.SLDPRT`.
- Export printable files with the same base name as the SolidWorks part.

Example:

```text
01_Body_Shell_Main.SLDPRT
01_Body_Shell_Main_R02.3mf
01_Body_Shell_Main_R02.stl
```
