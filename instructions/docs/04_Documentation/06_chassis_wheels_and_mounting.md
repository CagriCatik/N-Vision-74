# 06 - Chassis, Wheels, and Mounting Design

## Separate body and chassis

Do not model the body and chassis as one fixed block. Keep them separate so they can be printed, assembled, repaired, and modified independently.

Recommended assembly structure:

```text
Vehicle_1_10_Master.SLDASM
├── Body assembly
├── Chassis assembly
├── Wheel assembly
├── Interior assembly
└── Detail parts
```

## Static display chassis

For a static model, the chassis can be simple.

Minimum features:

- base plate,
- axle supports,
- wheel mounting holes,
- body mounting points,
- optional interior tub support,
- optional display stand holes.

Recommended starting dimensions:

```text
Chassis plate thickness: 3-5 mm
Rib thickness: 2-3 mm
Screw boss height: 5-10 mm
Body clearance: 0.5-1.0 mm
```

## Functional RC chassis

For an RC-capable 1:10 vehicle, use a modular chassis.

Recommended modules:

```text
Main chassis plate
Front suspension carrier
Rear suspension carrier
Battery tray
Servo mount
Motor mount
ESC/receiver tray
Cable routing clips
Body mount structure
Bumper/crash structures
```

## Chassis stiffness

FDM-printed parts can flex or crack along layer lines. Add stiffness using:

- ribs,
- boxed sections,
- fillets,
- triangular gussets,
- metal rods or plates where needed,
- separate replaceable high-load parts.

Avoid sharp internal corners. Add fillets to stress areas.

Starting fillet values:

```text
Cosmetic fillets: 0.5-1.0 mm
Structural internal fillets: 1.5-3.0 mm
Chassis rib root fillets: 2.0-4.0 mm
```

## Wheel design

Model wheels separately.

Wheel parameters:

```text
Outer tire diameter
Rim diameter
Tire width
Wheel offset
Hub diameter
Axle hole diameter
Bearing size if functional
```

For a static model:

- wheel and tire can be one printed part,
- use simplified hub detail,
- axle can be a printed pin or metal rod.

For a functional RC model:

- use real bearings,
- use metal axles or shafts,
- design replaceable hubs,
- use screws instead of fragile printed clips.

!!! warning
    Avoid printed high-load shafts.

## Wheel arch clearance

For a static model:

```text
Minimum wheel-to-arch clearance: 1-2 mm
```

For an RC model:

```text
Steering clearance: check full left/right lock
Suspension compression clearance: check full bump position
Wheel-to-body clearance: 3-8 mm depending on suspension travel
```

## Steering clearance check in SolidWorks

1. Insert wheel and tire assembly.
2. Mate wheel centre to axle location.
3. Create steering angle positions, for example 0, 20, and 30 degrees.
4. Use `Move Component` or angle mates.
5. Use `Interference Detection`.
6. Check wheel arch, bumper, side skirt, and chassis interference.

## Body-to-chassis mounting

Possible mounting methods:

### Screw mounting

Best for static and robust display models.

Design:

```text
Internal body boss
Chassis clearance hole
M2/M3 screw
Washer if needed
```

### Magnet mounting

Good for clean display models.

Design:

```text
Magnet pocket in body
Matching magnet pocket in chassis
Adhesive retention
Polarity check before gluing
```

### RC body posts

Useful for functional RC vehicles but visually less realistic.

Design:

```text
Vertical posts from chassis
Body shell holes
Body clips or screw caps
```

## Recommended fasteners

For 1:10 printed parts:

```text
M2 screws: small details and light brackets
M2.5 screws: medium detail parts
M3 screws: chassis, body mounts, structural areas
Heat-set inserts: repeated assembly/disassembly
Self-tapping screws: quick prototypes only
```
