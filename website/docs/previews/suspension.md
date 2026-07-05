# Suspension Components

Interactive 3D preview of the N-Vision-74 suspension system.

## Overview

The suspension system provides controlled movement and stability through the front and rear independent suspensions with shock absorbers.

## Front Suspension Assembly

The front suspension uses a double-wishbone design with shock absorbers.

**Key Components:**
- Tower Assembly
- Upper and Lower Control Arms
- Shock Absorbers (2)
- Ball Joints and Tie Rods

### Front Tower

**Part Number:** Front_Tower.SLDPRT  
**Material:** Aluminum  
**Weight:** ~45g

Features:
- Precision-drilled mounting points
- Accommodates arm pivots
- Shock absorber mount points
- Steering linkage attachment

### Front Control Arms

**Upper Arm Part:** Front_arm_Top_L/R.SLDPRT  
**Lower Arm Part:** Front_arm_bottom_L/R.SLDPRT  
**Material:** Aluminum 7075 (high strength)  
**Weight:** ~12g each

Design Features:
- High-strength aluminum alloy
- Optimized for rigidity
- Ball joint compatible
- Ackermann geometry for handling

### Front Hub

**Part Number:** Front_hub_L/R.SLDPRT  
**Material:** Aluminum  
**Weight:** ~8g

- Wheel mounting interface
- Bearing housing
- Brake carrier mount
- Tie rod connection point

## Rear Suspension Assembly

The rear suspension mirrors the front with independent control arms.

**Key Components:**
- Tower Assembly
- Upper and Lower Control Arms
- Shock Absorbers (2)
- Ball Joints and Tie Rods

### Rear Tower

**Part Number:** Rear_Tower.SLDPRT  
**Material:** Aluminum  
**Weight:** ~45g

Features:
- Structural mount point
- Multi-point arm attachment
- Shock mount compatibility
- Reinforced for durability

### Rear Control Arms

**Rear Arm Part:** Rear_arm_L/R.SLDPRT  
**Material:** Aluminum 7075  
**Weight:** ~14g each

Design:
- Longer arms for compliance
- Wider stance for stability
- Optimized for rear weight bias
- Adjustable length for tuning

#### Left Rear Control Arm 3D Preview

<div class="stl-viewer" data-src="assets/stls/left-rear-lower-control-arm.stl" data-color="#2563eb" data-autorotate="false"></div>

#### Right Rear Control Arm 3D Preview

<div class="stl-viewer" data-src="assets/stls/right-rear-lower-control-arm.stl" data-color="#2563eb" data-autorotate="false"></div>

### Rear Hub

**Part Number:** Rear_hub_L/R.SLDPRT  
**Material:** Aluminum  
**Weight:** ~10g

- Wheel mounting interface
- Bearing housing
- Optimized for load bearing
- Tie rod mount point

## Shock Absorber System

**Type:** Coil-over shock absorber  
**Stroke:** 60mm  
**Spring Rate:** Adjustable  
**Oil:** Shock oil (suspension fluid)

### Specifications

| Parameter | Value |
|-----------|-------|
| Compressed Length | 100mm |
| Extended Length | 160mm |
| Stroke | 60mm |
| Eye-to-Eye | 50mm |
| Mounting | Ball joint (both ends) |

### Installation
1. Mount upper ball joint to arm mount
2. Mount lower ball joint to chassis bracket
3. Ensure equal compression on all 4
4. Test smooth operation

## Tie Rod System

**Configuration:** Front and rear tie rods  
**Adjustability:** Full range length adjustment  
**Material:** Aluminum  
**Thread:** M4 standard

### Tie Rod Specifications

| Location | Part | Length | Adjustment |
|----------|------|--------|------------|
| Front | Tie_rod_M4 | 80mm | ±10mm |
| Rear | Tie_rod_M5 | 90mm | ±15mm |

### Toe Adjustment
- Front toe: 2mm total (1mm each side)
- Rear toe: 1mm total (0.5mm each side)
- Adjust by changing tie rod length

## Ball Joint & Lock System

**Part Number:** Ball_Lock.SLDPRT  
**Material:** Steel  
**Thread:** M3/M4  
**Quantity:** 8 total (4 per end)

Features:
- Spring-loaded locking mechanism
- Prevents accidental loosening
- Easy to install and remove
- Durable construction

## Suspension Geometry

### Front Suspension
- Camber: -2° to +2° (adjustable)
- Caster: 5°
- Toe: 0° to 4°
- Kingpin inclination: 10°

### Rear Suspension
- Camber: -1° to +1°
- Toe: 0° to 2°
- Tracking: Parallel to front

## Tuning Guide

### Stiff Suspension
**Use when:** Racing, smooth surfaces  
**Setup:**
- Stiffer spring rates
- Less shock oil viscosity
- Lower ride height

### Soft Suspension
**Use when:** Technical terrain, comfort  
**Setup:**
- Softer spring rates
- Higher shock oil viscosity
- Taller ride height

### Balance Tuning
1. Adjust shock preload equally
2. Change spring rates in pairs
3. Adjust ride height for weight distribution
4. Test and iterate

## Maintenance

### Shock Maintenance
- Check oil level monthly
- Look for leaks
- Replace seals if needed (~$15 per shock)
- Oil change every 6 months ($5 per shock)

### Arm Maintenance
- Check for cracks
- Verify pivot smoothness
- Inspect ball joints
- Clean out dirt/mud

### Tie Rod Maintenance
- Keep threads clean
- Apply light oil to threads
- Check for bending
- Verify lock nut tightness

## Replacement Parts

| Component | Cost | Lead Time |
|-----------|------|-----------|
| Shock Absorber | $20 | 1 week |
| Control Arm | $15 | 2 weeks |
| Tie Rod Set | $12 | 3 days |
| Ball Lock | $2 | 1 week |
| Tower Assembly | $35 | 2 weeks |

## Related Components

- [Chassis](chassis.md)
- [Wheels & Tires](chassis.md#wheels)
- [Technical Assembly](../technical/assembly.md)

---

**Component Version:** 1.0  
**Last Updated:** 2026-07-05
