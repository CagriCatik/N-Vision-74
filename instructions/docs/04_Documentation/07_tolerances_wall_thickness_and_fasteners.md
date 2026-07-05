# 07 - Tolerances, Wall Thickness, and Fasteners

## Why tolerances matter

SolidWorks geometry is exact. 3D-printed geometry is not. Printer calibration, material shrinkage, layer height, nozzle size, orientation, and slicer settings all affect real dimensions.

Design clearances intentionally.

## Starting values for FDM printing

| Feature | Starting value |
|---|---:|
| Body shell wall thickness | 1.6-2.4 mm |
| Structural chassis wall | 3.0-5.0 mm |
| Decorative detail minimum | 0.8-1.0 mm |
| Normal assembly clearance | 0.3-0.5 mm |
| Sliding clearance | 0.4-0.7 mm |
| Tight press-fit clearance | 0.1-0.2 mm, test required |
| Panel groove width | 0.5-0.8 mm |
| Panel groove depth | 0.3-0.6 mm |
| Minimum structural fillet | 1.5-3.0 mm |

!!! tip
    These are not universal rules. Always print tolerance samples.

## Hole sizing

Printed holes often come out smaller than designed, especially in FDM.

Starting offsets:

```text
M2 clearance hole: 2.2-2.4 mm
M2.5 clearance hole: 2.7-2.9 mm
M3 clearance hole: 3.2-3.4 mm
3.0 mm alignment pin hole: 3.2-3.4 mm
```

For precise holes, design slightly undersized and drill after printing, or use heat-set inserts.

## Screw bosses

Recommended boss design:

```text
Boss outer diameter: screw diameter x 2.5 to 3.0
Boss wall thickness: 1.2-2.0 mm
Fillet at base: 1.0-2.5 mm
Avoid unsupported tall bosses
Add ribs if boss is loaded
```

Example for M3:

```text
Screw: M3
Boss outer diameter: 7.5-9.0 mm
Clearance hole: 3.2-3.4 mm
Boss base fillet: 1.5-2.5 mm
```

## Heat-set inserts

Use heat-set inserts for repeated assembly.

Typical use:

- body-to-chassis mounts,
- battery tray,
- servo mount,
- removable bumpers,
- suspension modules.

Design notes:

- follow insert supplier hole diameter,
- leave enough wall thickness around insert,
- avoid placing inserts too close to thin exterior surfaces,
- print test coupons before final body print.

## Snap fits

!!! warning
    Snap fits are possible but risky in FDM depending on material and print direction. Use snap fits only after testing.

Better options for first prototype:

- screws,
- magnets,
- alignment pins plus adhesive,
- dovetail slides,
- replaceable clips.

## Layer orientation and strength

Printed parts are weaker between layers. For structural parts:

- orient load paths along layers where possible,
- avoid screw bosses loaded directly in layer separation,
- add fillets and ribs,
- use metal fasteners for high-load joints,
- avoid thin vertical tabs.

## Material suggestions

### PLA

Good for:

- first prototypes,
- static display models,
- dimensional checks.

Weaknesses:

- heat sensitivity,
- brittle snap fits,
- poor long-term car interior temperature resistance.

### PETG

Good for:

- functional prototypes,
- slightly flexible parts,
- chassis and mounts.

Weaknesses:

- stringing,
- less crisp details than PLA.

### ABS/ASA

Good for:

- painted body shells,
- higher temperature resistance,
- sanding and post-processing.

Weaknesses:

- warping,
- enclosure recommended,
- fumes and ventilation concerns.

### Resin

Good for:

- small details,
- lights,
- badges,
- interior parts.

Weaknesses:

- brittle for structural parts,
- large body shells can be difficult and expensive.
