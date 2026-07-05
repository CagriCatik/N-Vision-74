# Steering System Components

Interactive 3D preview of the N-Vision-74 steering system.

## Overview

The steering system provides directional control through servo-actuated linkages connected to the front wheels.

## Steering Tower Assembly

**Part Number:** Steering system assembly  
**Material:** Mixed (Aluminum + Steel)  
**Weight:** ~85g

### Components
- Tower structure
- Servo mount bracket
- Linkage attachment points
- Calibration reference marks

### Tower Features
- Precision-machined construction
- Multi-point attachment to chassis
- Quick-change servo interface
- Anti-vibration damping

## Steering Servo

**Type:** Digital Standard Servo  
**Specification:** 8 kg·cm torque  
**Response Time:** 0.18s per 60°

### Servo Mounting
1. Position servo in bracket
2. Align output shaft horizontally
3. Secure with servo clips
4. Connect to receiver channel 1
5. Calibrate center position

### Servo Control Signal
- Channel 1 from receiver
- Proportional input 1000-2000 μs
- Center position: 1500 μs
- Full left: 1000 μs
- Full right: 2000 μs

## Steering Linkage

### Servo Arm to Tower

**Connection Type:** Bell crank linkage  
**Material:** Aluminum  
**Movement:** ~45° total throw

**Installation Steps:**
1. Attach servo arm to servo output shaft
2. Connect servo arm to steering tower via ball link
3. Adjust length for neutral steering
4. Tighten lock nut firmly
5. Test full steering range

### Tower to Wheels

**Connection:** Tie rod assemblies (front and rear)  
**Material:** Aluminum  
**Thread:** M4 standard

## Tie Rod System

**Configuration:** Ackermann geometry  
**Adjustment:** Full range length modification  
**Material:** Aluminum tubes with threaded ends

### Front Tie Rod Specifications

| Parameter | Value |
|-----------|-------|
| Natural Length | 80mm |
| Adjustment Range | ±10mm |
| Thread Pitch | M4 |
| Material | Aluminum 6061 |
| Weight | ~3g |

### Rear Tie Rod Specifications

| Parameter | Value |
|-----------|-------|
| Natural Length | 90mm |
| Adjustment Range | ±15mm |
| Thread Pitch | M5 |
| Material | Aluminum 6061 |
| Weight | ~4g |

## Steering Geometry

### Ackermann Steering Principle
The inside wheel turns more sharply than the outside wheel for optimal cornering.

### Steering Angles

| Parameter | Specification |
|-----------|----------------|
| Total Steering Travel | 90° (45° each direction) |
| Inside Wheel Lock | 35° |
| Outside Wheel Lock | 25° |
| Toe Adjustment | -4° to +4° |
| Camber Adjustment | -3° to +3° |

### Toe-In Adjustment
**Purpose:** Wheel alignment parallel to vehicle centerline

**Procedure:**
1. Place vehicle on flat surface
2. Measure distance between wheel fronts (A)
3. Measure distance between wheel rears (B)
4. Front should be 2-4mm closer (A < B)
5. Adjust tie rod length to achieve toe

## Steering Response

### Servo Center Calibration
1. Power on ESC with throttle centered
2. Note servo position
3. Move steering trim to center
4. Servo should be mechanically centered
5. Adjust trim as needed

### Endpoint Adjustment
1. Steer full left
2. Measure wheel lock angle
3. Adjust servo endpoint if needed
4. Repeat for right side
5. Balance left and right travel

### Steering Sensitivity

| Setting | Effect | Use Case |
|---------|--------|----------|
| Standard | 1:1 input ratio | General driving |
| Sensitive | 1:0.8 ratio | Technical terrain |
| Dampened | 1:1.2 ratio | High-speed racing |

## Left Steering Arm

**Part Number:** Left_shaft_arm.SLDPRT  
**Material:** Steel  
**Weight:** ~15g

### Features
- M4 threaded connection point
- Reinforced for durability
- Offset geometry for mechanical advantage
- Joint for ball links

## Right Tower Lower

**Part Number:** Right_tower_lower.SLDPRT  
**Material:** Aluminum  
**Weight:** ~20g

### Integration Points
- Main tower mounting interface
- Tie rod connection points
- Geometric reference marks
- Calibration datum

## Ball Link System

**Type:** M3/M4 threaded ball joint  
**Material:** Steel  
**Durability:** Rated for full steering travel

### Installation
1. Screw ball link into threaded hole
2. Tighten until snug (don't over-tighten)
3. Connect vehicle link
4. Verify smooth articulation
5. Apply lock-tight if needed

### Ball Link Replacement
- Standard M3/M4 threads
- Readily available replacement parts
- Cost: $2-5 per link
- Installation time: 2-3 minutes

## Steering Specifications

### Physical Dimensions

| Measurement | Value |
|-------------|-------|
| Wheelbase | 260mm |
| Track Width | 220mm |
| Steering Tower Height | 45mm |
| Tie Rod Length (neutral) | 85mm (front), 95mm (rear) |

### Performance Metrics

| Metric | Value |
|--------|-------|
| Steering Ratio | 8:1 (approximate) |
| Lock-to-Lock Time | 1.2 seconds |
| Wheel Lock Angle | 35° inside, 25° outside |
| Minimum Turn Radius | ~0.3m |

## Tuning Guide

### Under-Steer (Vehicle Won't Turn)
**Causes:**
- Tie rods too long
- Toe-in excessive
- Servo endpoint limited

**Solutions:**
1. Shorten front tie rods
2. Reduce toe-in
3. Increase servo endpoints
4. Verify servo power

### Over-Steer (Vehicle Over-Responds)
**Causes:**
- Tie rods too short
- Negative toe-out
- Excessive servo sensitivity

**Solutions:**
1. Lengthen front tie rods
2. Adjust toe toward neutral
3. Reduce servo sensitivity
4. Check for loose joints

### Pulling to One Side
**Causes:**
- Unequal servo throw
- Bent tie rod
- Misaligned hub

**Solutions:**
1. Balance steering trim
2. Verify tie rod straightness
3. Check wheel alignment
4. Test on different surface

## Maintenance Schedule

### Before Each Run
- [ ] Check servo response
- [ ] Verify tie rod tightness
- [ ] Test steering smoothness
- [ ] Check for looseness

### Weekly Maintenance
- [ ] Deep clean steering components
- [ ] Inspect for cracks/bending
- [ ] Test full steering range
- [ ] Verify servo centering

### Monthly Service
- [ ] Re-torque all fasteners
- [ ] Apply light oil to threads
- [ ] Inspect ball joints
- [ ] Check servo gears for wear

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| Steering lag | Servo slow | Replace servo, check power |
| Binding | Tight joints | Loosen slightly, clean |
| Loose steering | Worn ball joints | Replace ball links |
| Uneven response | Servo damage | Recalibrate or replace |
| Wheel wobble | Loose tie rod | Tighten lock nut |

## Spare Parts Kit

### Recommended Spares
- Servo: 1 (for replacement)
- Ball links: 8 (M3 & M4)
- Tie rods: 2 sets (front & rear)
- Servo clips: 2 sets
- Fasteners (M3-M4): Assorted

### Storage Organization
- Label each spare part
- Keep in sealed container
- Store with desiccant
- Inventory check monthly

## Advanced Tuning

### Pro Setup Tips
1. **Ackermann Calibration** - Precise toe adjustment
2. **Servo Curve** - Non-linear response programming
3. **Dual Rate** - Different sensitivity per speed
4. **Exponential** - Smoother low-speed control

## Performance Impact

### Steering Geometry on Handling

| Adjustment | Effect | Racing | Trail |
|------------|--------|--------|-------|
| Increased toe | More direct | Better | Twitchy |
| More camber | Better cornering | Improved | Tire wear |
| Longer tie rods | Smoother | Stable | Less responsive |
| Servo upgrade | Faster response | Competitive | Precision |

## Related Systems

- [Electronics & Servo](electronics.md)
- [Suspension](suspension.md)
- [Chassis](chassis.md)
- [Technical Assembly Guide](../technical/assembly.md)

---

**Component Version:** 1.0  
**Last Updated:** 2026-07-05
