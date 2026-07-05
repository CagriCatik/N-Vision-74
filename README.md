# N-Vision-74: 1:10 Scale Hyundai N Vision 74 CAD & 3D Printing Project

A comprehensive repository for modeling, scaling, and preparing a 1:10 scale physical model of the Hyundai N Vision 74 concept car for 3D printing fabrication, based on SolidWorks best practices and assembly-driven design methodology.

## 📋 Quick Links

- **🌐 [Live Documentation](http://localhost:8000)** - Interactive project documentation with 3D previews
- **📚 [Project Goals](#project-goals)** - What this project is about
- **📂 [Repository Structure](#repository-structure)** - How files are organized
- **🚀 [Getting Started](#getting-started)** - Quick start guide
- **🛠️ [Software Requirements](#software-requirements)** - Tools you'll need
- **📖 [Full Documentation](#full-documentation)** - Detailed workflow guide

---

## 🎯 Project Overview

This is a **fabrication-oriented CAD project** that takes the iconic Hyundai N Vision 74 concept car and translates it into a manufacturable 1:10 scale model. The project emphasizes:

- **Clean CAD workflow** separating design geometry from fabrication outputs
- **Assembly-driven structure** for easy modification and iteration
- **Print-ready segmentation** optimized for 3D printer build volumes
- **Comprehensive documentation** for reproducibility and knowledge sharing

<p align="center">
  <img src="assets/Hyundai_N_Vision_74_Concept.jpg" alt="Hyundai N Vision 74 Concept" width="70%">
</p>

---

## 🎬 Project Goals

- ✅ Recreate the exterior of the Hyundai N Vision 74 concept as a 1:10 scale CAD model
- ✅ Practice advanced surfacing and parametric modeling with fabrication-oriented workflow
- ✅ Maintain clean separation between design geometry (CAD) and fabrication outputs (STL, STEP, etc.)
- ✅ Document scale, tolerances, and print-specific modifications for reproducible results
- ✅ Create a modular design that supports easy customization and iteration

---

## 📏 Scale and Context

### Target Specifications

| Specification | Value |
|---------------|-------|
| **Original Scale** | 1:1 (full-size Hyundai N Vision 74) |
| **Model Scale** | 1:10 |
| **Scale Factor** | 0.1 (all linear dimensions) |
| **Design Approach** | Assembly-driven SolidWorks methodology |
| **Output Formats** | STL, 3MF, STEP, PDF |

### Key Considerations for 1:10 Printable Model

- **Wall Thickness**: Minimum 2-3mm compatible with standard FDM printers
- **Part Segmentation**: Body split into logical modules for printing and assembly
- **Assembly Features**: Pins, tabs, and overlaps built directly into CAD
- **Clearances**: Press-fit and glue-joint offsets pre-calculated
- **Support Design**: Print-friendly geometries that minimize support structures

---

## 📂 Repository Structure

The repository is organized to support both CAD development and fabrication workflows:

```
N-Vision-74/
├── 01_Blueprints/                    # Reference images (side, top, front, rear views)
├── 02_Reference_Dimensions/          # Real vehicle dimensions and 1:10 scale calculations
├── 03_SolidWorks_Project/            # Main CAD files
│   ├── Vehicle_1_10_Master.SLDASM    # Master assembly (all parts)
│   ├── 00_Master_Layout.SLDPRT       # Reference plate
│   ├── 01_Body_Shell_Main.SLDPRT     # Main shell
│   ├── 02_Body_Front_Bumper.SLDPRT   # Front bumper
│   ├── 03_Body_Rear_Bumper.SLDPRT    # Rear bumper
│   ├── 04_Chassis_Main_Plate.SLDPRT  # Main chassis
│   ├── 05_Chassis_Front_Module.SLDPRT
│   ├── 06_Chassis_Rear_Module.SLDPRT
│   ├── 07_Wheel.SLDPRT
│   ├── 08_Tire.SLDPRT
│   ├── 09_Mirror_Left.SLDPRT
│   ├── 10_Mirror_Right.SLDPRT
│   ├── 11_Light_Housings.SLDPRT
│   ├── 12_Interior_Tub.SLDPRT
│   └── [Suspension, Drivetrain, Electronics, Steering components]
├── 04_Documentation/                 # Markdown documentation chapters
├── 05_Checklists/                    # CAD, printability, and assembly checklists
├── 06_Resources/                     # Online resources and reference notes
├── 07_STL_Exports/                   # Exported STL/3MF/STEP files for 3D printing
├── 08_Print_Iterations/              # Test prints, photos, and revision notes
├── 09_Printer_and_Material_Profiles/ # Printer/material-specific configurations
├── website/                          # Interactive documentation (Zensical/Material theme)
├── assets/                           # Reference images and renders
├── blueprints/                       # Blueprint variations (colors, resolutions)
├── requirements.txt                  # Python dependencies for documentation server
├── README.md                         # This file
└── .github/                          # GitHub configuration

```

### Directory Purpose Reference

| Directory | Purpose |
|-----------|---------|
| `01_Blueprints/` | Side, top, front, rear blueprint images for reference |
| `02_Reference_Dimensions/` | Scale calculations, measurements, and dimensional analysis |
| `03_SolidWorks_Project/` | All CAD source files (native .SLDPRT and .SLDASM) |
| `04_Documentation/` | Detailed markdown guides and technical documentation |
| `05_Checklists/` | Printability checks, CAD verification, assembly guides |
| `06_Resources/` | Video links, online resources, and reference materials |
| `07_STL_Exports/` | Final STL/3MF files ready for 3D printer slicing |
| `08_Print_Iterations/` | Test print results, photos, and slicer configurations |
| `09_Printer_and_Material_Profiles/` | Printer settings for Bambu Lab P1S, A1 mini, and materials |
| `website/` | Live interactive documentation with 3D component previews |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CagriCatik/N-Vision-74.git
cd N-Vision-74
```

### 2. Set Up Python Environment (for Documentation Server)

```bash
# Create virtual environment
python -m venv venv

# Activate venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Start Interactive Documentation Server

```bash
cd website
zensical serve --dev-addr localhost:8000 --open
```

The documentation will open at `http://localhost:8000` with interactive 3D component previews.

### 4. Open SolidWorks Project

1. Navigate to `03_SolidWorks_Project/`
2. Open `Vehicle_1_10_Master.SLDASM` in SolidWorks
3. Verify all parts load correctly (should show ~50 parts)
4. Review the assembly structure to understand the design

---

## 🛠️ Software Requirements

### Required Software

| Software | Purpose | Version |
|----------|---------|---------|
| **SolidWorks** | CAD design and modeling | 2021+ (2023 recommended) |
| **Python** | Documentation server | 3.8+ |
| **Git** | Version control | Latest |

### Required Tools (Recommended)

| Tool | Purpose |
|------|---------|
| PrusaSlicer or Cura | 3D printer slicing |
| Meshmixer or Netfabb | STL mesh inspection and repair |
| Image viewer/editor | Blueprint preparation |

### Python Dependencies

All Python packages are listed in `requirements.txt`:

```
zensical>=0.0.46
mkdocs-material>=9.6.7
mkdocs-glightbox>=0.3.2
pymdown-extensions>=10.14.3
```

---

## 📖 How to Use This Repository

### For CAD Development

1. **Open Master Assembly**: Load `03_SolidWorks_Project/Vehicle_1_10_Master.SLDASM`
2. **Verify Scale**: All dimensions are already at 1:10 scale
3. **Review Naming Convention**: Parts follow `[Number]_[Component_Name].SLDPRT`
4. **Modify Components**: Edit individual parts in `03_SolidWorks_Project/`
5. **Create Revisions**: Use `_R02`, `_R03` suffix for iterations
6. **Export Fabrication Files**: 
   - STL to `07_STL_Exports/`
   - STEP to `07_STL_Exports/`

### For 3D Printing

1. **Review Checklists**: Check `05_Checklists/printer_material_decision_checklist.md`
2. **Select Printer Profile**: Review `09_Printer_and_Material_Profiles/`
3. **Prepare STL Files**: Use files from `07_STL_Exports/`
4. **Configure Slicer**: 
   - Wall thickness: 2-3mm minimum
   - Infill: 15-20%
   - Supports: as needed for overhangs
5. **Document Results**: Add photos and notes to `08_Print_Iterations/`

### For Documentation

1. **Read in Order**:
   - `04_Documentation/01_project_goal_and_scale.md`
   - `04_Documentation/02_blueprint_preparation_and_import.md`
   - `04_Documentation/03_solidworks_master_layout.md`
   - ... (continue through all chapters)

2. **Reference Checklists**: Use files in `05_Checklists/` during CAD work
3. **Track Progress**: Update this README as project evolves
4. **Share Results**: Add photos to `assets/`

---

## 📚 Full Documentation

### Recommended Reading Order

1. **Project Planning**
   - `04_Documentation/01_project_goal_and_scale.md` - Understanding the vision
   - `02_Reference_Dimensions/` - Vehicle dimensions and scale calculations

2. **Blueprint & Reference Setup**
   - `04_Documentation/02_blueprint_preparation_and_import.md` - Preparing reference images
   - `01_Blueprints/` - Blueprint images in various resolutions

3. **CAD Methodology**
   - `04_Documentation/03_solidworks_master_layout.md` - Assembly structure
   - `04_Documentation/04_body_surface_modeling_workflow.md` - Surfacing techniques
   - `03_SolidWorks_Project/` - Examine actual CAD files

4. **Fabrication & Printing**
   - `04_Documentation/05_printable_body_shell_and_splitting.md` - Print segmentation
   - `04_Documentation/06_chassis_wheels_and_mounting.md` - Assembly design
   - `04_Documentation/07_tolerances_wall_thickness_and_fasteners.md` - Critical specs
   - `04_Documentation/08_export_slicing_and_iteration.md` - Export workflow
   - `09_Printer_and_Material_Profiles/` - Printer-specific notes

5. **Troubleshooting & Best Practices**
   - `04_Documentation/09_common_mistakes_and_troubleshooting.md` - Lessons learned
   - `04_Documentation/10_bambu_lab_p1s_a1mini_material_strategy.md` - Material selection
   - `05_Checklists/` - Verification checklists

---

## 🔧 Modeling and Printing Notes

### Scale and Key Dimensions

- **Target Scale**: 1:10
- **Model Scale Factor**: 0.1× all dimensions
- **Design Approach**: Assembly-driven, component-based
- **Wall Thickness Target**: 2.0-3.0mm (FDM compatible)
- **Minimum Feature Size**: 3mm (depends on printer nozzle)

### Design Philosophy

- **Assembly-First**: Design as complete assemblies before splitting for print
- **Print-Oriented**: Include assembly features (pins, tabs) in CAD
- **Modular**: Each component should be independently printable
- **Documented**: All design decisions recorded in CAD comments and files
- **Iterated**: Test prints drive design refinement

### SolidWorks Workflow

1. **Reference Setup**: Sketch from blueprint images
2. **Parametric Modeling**: Use equations for scaling consistency
3. **Assembly Constraints**: Proper mates for design intent
4. **Configurations**: Alternative designs without duplicating files
5. **Part Naming**: Clear, version-controlled part names

---

## 🎯 Roadmap

### Phase 1: Design Foundation (Current)

- ✅ Set up reference images and base sketches at 1:10 scale
- ✅ Define main volumes and character lines for the body
- ✅ Create basic assembly structure with all major components
- ⏳ Complete primary surfacing with curvature continuity

### Phase 2: Detailing & Optimization

- ⏳ Add details: wheel arches, wheels, lights, grills, vents, mirrors
- ⏳ Refine geometry for better proportions
- ⏳ Optimize for print-friendly designs
- ⏳ Create segmentation for printing

### Phase 3: Fabrication & Testing

- ⏳ Finalize 1:10 configuration with verified dimensions
- ⏳ Segment model for printing (body modules, wheels, interior)
- ⏳ Integrate assembly features (pins, sockets, flanges)
- ⏳ Export and verify STLs (manifold, normals, quality)
- ⏳ Test prints of sample parts
- ⏳ Iterate based on print results

### Phase 4: Final Assembly & Documentation

- ⏳ Produce full model prints
- ⏳ Post-processing and finishing
- ⏳ Final assembly and photography
- ⏳ Document results and lessons learned
- ⏳ Create assembly guide for reproduction

---

## 🔗 Reference Materials

### Tutorial Series

This project is based on:
- **[SolidWorks CAD Tutorials](https://www.youtube.com/watch?v=qYp9NtI7Ol8&list=PLrXLIrXkHxeolVexRLXKaV8sT8K6MMKDX&index=2)** - Foundation modeling techniques

### Related Resources

- SolidWorks parametric design best practices
- 3D print design and tolerance guidelines
- FDM printing optimization for automotive models
- Assembly-driven CAD methodologies

---

## 💡 Key Principles

### CAD Design

> **Do not design only a beautiful model. Design a printable, segmented, assembled, repairable 1:10 product.**

- Components are designed as individual printable parts
- Assembly features are built into CAD, not post-processed
- Tolerances account for 3D printer precision (±0.2-0.5mm)
- Design is iterative—test prints drive refinement

### Print Strategy

> **Optimize for your printer, not just for aesthetics.**

- Primary printer: **Bambu Lab P1S** (large PLA/ABS parts)
- Secondary printer: **Bambu Lab A1 mini** (small parts, fit checks)
- Material selection: PLA for prototyping, ABS for final assembly
- Every part must be tested at actual print scale

### Documentation

> **If it's not documented, it didn't happen.**

- All design decisions recorded in CAD files and markdown
- Print results documented with photos and settings
- Tolerances verified against actual prints
- Lessons learned captured for future iterations

---

## 📝 Naming Convention

All CAD files follow a consistent naming pattern:

```
[Number]_[Component_Name].SLDPRT          # Initial version
[Number]_[Component_Name]_R02.SLDPRT      # Revision 2
[Number]_[Component_Name]_R02.stl         # STL export matching part
[Number]_[Component_Name]_R02.3mf         # 3MF export
```

**Examples:**
- `01_Body_Shell_Main.SLDPRT` – Initial release
- `04_Chassis_Main_Plate_R02.SLDPRT` – Revised version
- `07_Wheel_R01.stl` – Export for 3D printing

---

## 🤝 Contributing

### How to Contribute

1. **Document Your Work**: Add notes to `04_Documentation/` or `08_Print_Iterations/`
2. **Share Improvements**: Create branches for new features or optimizations
3. **Report Issues**: Document problems in `05_Checklists/` or GitHub issues
4. **Share Results**: Add photos to `assets/` and document in README

### Updating This README

- Update progress sections as phases complete
- Add new dimensions as they're verified
- Document lessons learned immediately
- Keep directory structure synchronized with actual files

---

## 📞 Support & Questions

### Documentation

- **Interactive Website**: Start local server and visit `/docs/`
- **Markdown Guides**: Read `04_Documentation/` files
- **CAD Examples**: Open and inspect SolidWorks files directly

### Troubleshooting

- Check `04_Documentation/09_common_mistakes_and_troubleshooting.md`
- Review `05_Checklists/` for verification steps
- Examine `08_Print_Iterations/` for similar problems

---

## 📄 License

Specify your project license here (e.g., MIT, CC-BY-4.0, etc.)

---

## 🙏 Acknowledgments

- **Original Design**: Hyundai N Vision 74 Concept
- **Tutorial Series**: [SolidWorks CAD Tutorials](https://www.youtube.com/watch?v=qYp9NtI7Ol8&list=PLrXLIrXkHxeolVexRLXKaV8sT8K6MMKDX&index=2)
- **3D Printing Community**: Best practices and optimization techniques
- **Project Team**: Contributors and testers

---

**Last Updated:** 2026-07-05  
**Project Status:** ✅ Active Development (Phase 1-2)  
**Latest Version:** 1.0
