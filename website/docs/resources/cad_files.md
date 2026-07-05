# CAD Source Files

Complete SolidWorks project files for the N-Vision-74 vehicle.

## Project Overview

**Project Name:** Vehicle_1_10_Master  
**Format:** SolidWorks 2023+  
**Total Size:** 450 MB (uncompressed)  
**Last Updated:** 2026-07-05  
**Status:** Complete and Production-Ready

## Main Assembly Structure

### Master Assembly File

**File:** Vehicle_1_10_Master.SLDASM  
**Description:** Main vehicle assembly containing all subassemblies  
**Size:** 12 MB  
**Status:** Ready for use

**Contains:**
- 13 main subassemblies
- 50+ individual parts
- All constraints and relationships
- Design intent documentation

## Assembly Hierarchy

```
Vehicle_1_10_Master.SLDASM
├── Body_Shell_Assembly.SLDASM
│   ├── 01_Body_Shell_Main.SLDPRT
│   ├── 02_Body_Front_Bumper.SLDPRT
│   ├── 03_Body_Rear_Bumper.SLDPRT
│   ├── 09_Mirror_Left.SLDPRT
│   ├── 10_Mirror_Right.SLDPRT
│   ├── 11_Light_Housings.SLDPRT
│   └── 12_Interior_Tub.SLDPRT
│
├── Chassis_Assembly.SLDASM
│   ├── 00_Master_Layout.SLDPRT
│   ├── 04_Chassis_Main_Plate.SLDPRT
│   ├── 05_Chassis_Front_Module.SLDPRT
│   └── 06_Chassis_Rear_Module.SLDPRT
│
├── Suspension_Assembly.SLDASM
│   ├── Front_Suspension.SLDASM
│   ├── Rear_Suspension.SLDASM
│   └── Shock_System.SLDASM
│
├── Drivetrain_Assembly.SLDASM
│   ├── Differential_Assembly.SLDASM
│   ├── Motor_Mount.SLDASM
│   └── Axle_System.SLDASM
│
├── Electronics_Assembly.SLDASM
│   ├── ESC_Mounting.SLDASM
│   ├── Battery_System.SLDASM
│   └── Cooling_System.SLDASM
│
└── Steering_Assembly.SLDASM
    ├── Servo_Mount.SLDASM
    ├── Steering_Linkage.SLDASM
    └── Tie_Rod_System.SLDASM
```

## Individual Part Files

### Body & Shell Components (Part 01-12)

| Part # | File Name | Description | Material | Status |
|--------|-----------|-------------|----------|--------|
| 00 | Master_Layout.SLDPRT | Reference plate | Steel | Rev 01 |
| 01 | Body_Shell_Main.SLDPRT | Main shell | PC | Rev 01 |
| 02 | Body_Front_Bumper.SLDPRT | Front bumper | TPU | Rev 01 |
| 03 | Body_Rear_Bumper.SLDPRT | Rear bumper | TPU | Rev 01 |
| 04 | Chassis_Main_Plate.SLDPRT | Main plate | Aluminum | Rev 02 |
| 05 | Chassis_Front_Module.SLDPRT | Front section | Aluminum | Rev 01 |
| 06 | Chassis_Rear_Module.SLDPRT | Rear section | Aluminum | Rev 01 |
| 07 | Wheel.SLDPRT | Wheel assembly | Aluminum | Rev 01 |
| 08 | Tire.SLDPRT | Tire/tread | Rubber | Rev 01 |
| 09 | Mirror_Left.SLDPRT | Left mirror | Plastic | Rev 01 |
| 10 | Mirror_Right.SLDPRT | Right mirror | Plastic | Rev 01 |
| 11 | Light_Housings.SLDPRT | Light assembly | Plastic | Rev 01 |
| 12 | Interior_Tub.SLDPRT | Floor panel | Plastic | Rev 01 |

## Suspension Components

### Front Suspension Assembly

| File | Description | Material | Weight |
|------|-------------|----------|--------|
| Front_Tower.SLDPRT | Tower structure | Aluminum | 45g |
| Front_arm_Top_L.SLDPRT | Upper arm left | Aluminum 7075 | 12g |
| Front_arm_Top_R.SLDPRT | Upper arm right | Aluminum 7075 | 12g |
| Front_arm_bottom_L.SLDPRT | Lower arm left | Aluminum 7075 | 12g |
| Front_arm_bottom_R.SLDPRT | Lower arm right | Aluminum 7075 | 12g |
| Front_hub_L.SLDPRT | Hub left | Aluminum | 8g |
| Front_hub_R.SLDPRT | Hub right | Aluminum | 8g |
| Front_arm_holder_front.SLDPRT | Holder front | Plastic | 5g |
| Front_arm_holder_rear.SLDPRT | Holder rear | Plastic | 5g |
| Shock_adapter_1_2x.SLDPRT | Adapter 1 (2×) | Plastic | 3g |
| Shock_adapter_2_2x.SLDPRT | Adapter 2 (2×) | Plastic | 3g |
| Front_center_brace_holder.SLDPRT | Brace holder | Plastic | 4g |
| Tie_rod_M4_1.SLDPRT | Tie rod 1 | Aluminum | 3g |
| Tie_rod_M4_2.SLDPRT | Tie rod 2 | Aluminum | 3g |

### Rear Suspension Assembly

| File | Description | Material | Weight |
|------|-------------|----------|--------|
| Rear_Tower.SLDPRT | Tower structure | Aluminum | 45g |
| Rear_arm_L.SLDPRT | Arm left | Aluminum 7075 | 14g |
| Rear_arm_R.SLDPRT | Arm right | Aluminum 7075 | 14g |
| Rear_hub_L.SLDPRT | Hub left | Aluminum | 10g |
| Rear_hub_R.SLDPRT | Hub right | Aluminum | 10g |
| Rear_arm_holder_front.SLDPRT | Holder front | Plastic | 5g |
| Rear_arm_holder_rear.SLDPRT | Holder rear | Plastic | 5g |
| Rear_brace_holder.SLDPRT | Brace holder | Plastic | 4g |
| Shock_adapter_1_2x.SLDPRT | Adapter 1 (2×) | Plastic | 3g |
| Shock_adapter_2_2x.SLDPRT | Adapter 2 (2×) | Plastic | 3g |
| Tie_rod_M5_1.SLDPRT | Tie rod 1 | Aluminum | 4g |
| Tie_rod_M5_2.SLDPRT | Tie rod 2 | Aluminum | 4g |

## Drivetrain Components

### Differential Assembly

| File | Description | Material | Status |
|------|-------------|----------|--------|
| Center_diff_top.SLDPRT | Top half | Aluminum | Rev 01 |
| Center_diff_bottom.SLDPRT | Bottom half | Aluminum | Rev 01 |
| Center_diff_top_cover.SLDPRT | Top cover | PC | Rev 01 |
| Diff_cover.SLDPRT | Access cover | Aluminum | Rev 01 |
| Diff_sway_bar_cover.SLDPRT | Sway bar cover | Plastic | Rev 01 |

### Motor & Drivetrain

| File | Description | Material | Notes |
|------|-------------|----------|-------|
| Motor_support_mount_1.SLDPRT | Mount 1 | Aluminum | Adjustable |
| Motor_support_mount_2.SLDPRT | Mount 2 | Aluminum | Adjustable |
| Motor_support_mount_3.SLDPRT | Mount 3 | Aluminum | Adjustable |
| Center_brace_holder.SLDPRT | Brace holder | Aluminum | Reinforcement |

## Electronics Components

| File | Description | Material | Weight |
|------|-------------|----------|--------|
| Battery_tray_L.SLDPRT | Left tray | Plastic | 10g |
| Battery_tray_R.SLDPRT | Right tray | Plastic | 10g |
| Ele_box_body_ESC.SLDPRT | ESC enclosure | PC | 45g |
| Ele_box_body_WP8BL150.SLDPRT | Motor enclosure | PC | 35g |
| Ele_cover.SLDPRT | ESC cover | Plastic | 20g |
| Fan_shroud.SLDPRT | Cooling fan | Plastic | 12g |
| On_Off_switch_holder_WP8BL150.SLDPRT | Switch holder | Plastic | 5g |

## Steering Components

| File | Description | Material | Notes |
|------|-------------|----------|-------|
| Left_shaft_arm.SLDPRT | Steering arm | Steel | M4 thread |
| Right_tower_lower.SLDPRT | Tower lower | Aluminum | Precision |

## Design Standards

### Naming Convention

```
[NUMBER]_[COMPONENT_NAME].SLDPRT
[NUMBER]_[COMPONENT_NAME]_R[REVISION].SLDPRT
```

**Example:**
- `04_Chassis_Main_Plate.SLDPRT` - Revision 1
- `04_Chassis_Main_Plate_R02.SLDPRT` - Revision 2

### File Organization

All files are stored in the `03_SolidWorks_Project/` directory with these guidelines:

- Alphabetical part numbering (00-12+)
- Clear descriptive names
- Revision suffix only when changed
- Consistent units (mm)
- Color-coded assemblies

## Export Formats

### Available Formats

| Format | File Extension | Use Case | Size |
|--------|----------------|----------|------|
| SolidWorks | .SLDPRT, .SLDASM | Native editing | Large |
| STEP | .step | CAD import | Medium |
| IGES | .iges | Legacy CAD | Medium |
| STL | .stl | 3D printing | Small |
| 3MF | .3mf | Modern 3D | Small |
| PDF | .pdf | Documentation | Small |
| DWG | .dwg | 2D drawings | Small |

### Export Procedure

1. **Open part/assembly in SolidWorks**
2. **File → Save As**
3. **Select desired format**
4. **Choose save location**
5. **Name consistently with original**
6. **Verify exported file**

## Modification Guidelines

### Before Modifying

1. **Create backup** of original files
2. **Increment revision number** if changed
3. **Document all changes** in comments
4. **Update BOMs** if parts change
5. **Re-validate assembly** after changes

### Assembly Constraints

| Constraint | Purpose | Locked |
|-----------|---------|--------|
| Coincident | Alignment | Yes |
| Parallel | Geometry | Yes |
| Perpendicular | Geometry | Yes |
| Distance | Spacing | Adjustable |
| Angle | Rotation | Adjustable |

### Best Practices

- Use configurations for variants
- Create equations for parametric design
- Document design intent
- Use reference geometry
- Maintain revision history

## CAD File Access

### Project Repository Structure

```
03_SolidWorks_Project/
├── Vehicle_1_10_Master.SLDASM (main file)
├── Parts/
│   ├── Body/
│   ├── Chassis/
│   ├── Suspension/
│   ├── Drivetrain/
│   ├── Electronics/
│   └── Steering/
├── Assemblies/
│   ├── Body_Shell_Assembly.SLDASM
│   ├── Chassis_Assembly.SLDASM
│   ├── Suspension_Assembly.SLDASM
│   ├── Drivetrain_Assembly.SLDASM
│   ├── Electronics_Assembly.SLDASM
│   └── Steering_Assembly.SLDASM
├── Drawings/
│   ├── Assembly_Drawings/
│   ├── Detail_Drawings/
│   └── Exploded_Views/
└── Resources/
    ├── Materials/
    ├── Fasteners/
    └── References/
```

## System Requirements

### SolidWorks

- **Minimum:** SolidWorks 2021
- **Recommended:** SolidWorks 2023 or newer
- **RAM:** 8GB minimum, 16GB+ recommended
- **Disk Space:** 2GB free for project
- **GPU:** Graphics card with OpenGL 3.0+

### Alternative Software (Compatibility)

| Software | Compatibility | Notes |
|----------|---------------|-------|
| Fusion 360 | 95% | Good import support |
| FreeCAD | 80% | Some constraint loss |
| Onshape | 90% | Cloud-based |

## Support & Documentation

### Getting Started with Files

1. **Download** Vehicle_1_10_Master.zip
2. **Extract** to project directory
3. **Open** Vehicle_1_10_Master.SLDASM
4. **Verify** all parts load correctly
5. **Review** assembly structure

### Common Issues

| Issue | Solution |
|-------|----------|
| Missing parts | Check file paths |
| Failed constraints | Verify dimensions |
| Slow performance | Reduce graphics detail |
| Export errors | Update software |

### Help & Resources

- [SolidWorks Tutorials](#)
- [Design Documentation](#)
- [FAQ & Troubleshooting](#)
- [Community Forum](#)

## License & Usage

**License:** Creative Commons Attribution 4.0  
**Attribution:** N-Vision-74 Project  
**Commercial Use:** Allowed with attribution

## Version Control

| Version | Release Date | Changes |
|---------|--------------|---------|
| 1.0 | 2026-07-05 | Initial CAD release |
| 1.1 | Planned | Minor optimizations |
| 2.0 | Planned | Major redesign |

---

**Last Updated:** 2026-07-05  
**Maintained By:** N-Vision-74 Team
