# N-Vision-74 Documentation

Welcome to the N-Vision-74 project documentation — a fabrication-oriented guide to modeling, scaling, and 3D-printing a 1:10 scale Hyundai N Vision 74 concept car, based on an assembly-driven SolidWorks workflow.

## Project Overview

N-Vision-74 translates the Hyundai N Vision 74 concept into a manufacturable 1:10 scale model:

- **Blueprint-Driven Design** - Multi-resolution reference blueprints for accurate scaling
- **Assembly-Driven SolidWorks Structure** - Clean separation of design geometry and fabrication outputs
- **Print-Ready Segmentation** - Parts toleranced and split for FDM 3D printing
- **Interactive 3D Previews** - Inspect exported STL components directly in the browser

## Documentation Chapters

### [01 · Blueprints](01_Blueprints/README.md)

High-resolution reference blueprints (side, top, front, rear) in multiple resolutions and background variants for CAD sketching.

### [02 · Reference Dimensions](02_Reference_Dimensions/scale_calculation_template.md)

Real vehicle measurements and 1:10 scale calculations used to validate the CAD model.

### [03 · SolidWorks Project](03_SolidWorks_Project/solidworks_file_plan.md)

The assembly-driven file plan and master layout strategy behind the CAD structure.

### 04 · Documentation

The core step-by-step build guide, from project goal to final print iteration:

1. [Project Goal and 1:10 Scale Strategy](04_Documentation/01_project_goal_and_scale.md)
2. [Blueprint Preparation and Import into SolidWorks](04_Documentation/02_blueprint_preparation_and_import.md)
3. [SolidWorks Master Layout Strategy](04_Documentation/03_solidworks_master_layout.md)
4. [Body Surface Modelling Workflow](04_Documentation/04_body_surface_modeling_workflow.md)
5. [Printable Body Shell and Part Splitting](04_Documentation/05_printable_body_shell_and_splitting.md)
6. [Chassis, Wheels, and Mounting Design](04_Documentation/06_chassis_wheels_and_mounting.md)
7. [Tolerances, Wall Thickness, and Fasteners](04_Documentation/07_tolerances_wall_thickness_and_fasteners.md)
8. [Export, Slicing, and Print Iteration](04_Documentation/08_export_slicing_and_iteration.md)
9. [Common Mistakes and Troubleshooting](04_Documentation/09_common_mistakes_and_troubleshooting.md)
10. [Bambu Lab P1S, A1 mini, PLA/ABS Material Strategy](04_Documentation/10_bambu_lab_p1s_a1mini_material_strategy.md)

### 05 · Checklists

Verification checklists to run before committing to a print:

- [SolidWorks Modelling Checklist](05_Checklists/solidworks_modeling_checklist.md)
- [Printer and Material Decision Checklist](05_Checklists/printer_material_decision_checklist.md)
- [3D Printing Checklist](05_Checklists/3d_printing_checklist.md)

### 06 · Resources

- [Online Resources and Best Practices](06_Resources/online_resources.md)
- [Search Notes](06_Resources/search_notes.md)

### 07 · STL Exports

Final STL/3MF files ready for slicing, exported from the master assembly.

### [08 · Print Iterations](08_Print_Iterations/iteration_log_template.md)

Log template for tracking test prints, revisions, and lessons learned.

### 09 · Printer and Material Profiles

Printer-specific settings and measured results:

- [P1S PLA Profile Notes](09_Printer_and_Material_Profiles/p1s_pla_profile_notes.md)
- [P1S ABS Profile Notes](09_Printer_and_Material_Profiles/p1s_abs_profile_notes.md)
- [A1 mini PLA Profile Notes](09_Printer_and_Material_Profiles/a1mini_pla_profile_notes.md)
- [Tolerance Coupon Results](09_Printer_and_Material_Profiles/tolerance_coupon_results.md)

## 3D Component Previews

Interactive, in-browser previews of exported STL parts — drag to rotate, scroll to zoom. Source STL files live under `assets/stls/`.

- [Body & Shell Preview](previews/body_shell.md)

## Getting Help

For questions or issues:

1. Check the [04 · Documentation](04_Documentation/01_project_goal_and_scale.md) chapters for the full workflow
2. Review the [05 · Checklists](05_Checklists/solidworks_modeling_checklist.md) before committing to a print
3. Consult [09 · Printer and Material Profiles](09_Printer_and_Material_Profiles/p1s_pla_profile_notes.md) for printer-specific settings

---

**Version:** 1.0
**Last Updated:** 2026-07-05
