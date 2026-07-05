# Drivetrain Components

Interactive 3D preview of the N-Vision-74 drivetrain system.

## Overview

The drivetrain transfers power from the motor to all wheels through a center differential system.

## Center Differential Assembly

The differential distributes torque to front and rear axles.

**Part Number:** Center_diff_top.SLDPRT / Center_diff_bottom.SLDPRT  
**Material:** Aluminum  
**Weight:** ~60g (assembled)

### Main Components
- Differential housing (top and bottom)
- Helical gear set
- Cross-pin and shafts
- Side gears for axle drive

### Differential Specifications

| Specification | Value |
|---------------|-------|
| Type | Open differential (helical) |
| Gear Ratio | 3.73:1 standard |
| Max Torque | 80 Nm |
| Oil Capacity | 10ml |
| Temperature Limit | 80°C |

### Helical Gear Design
- Low noise operation
- Smooth power delivery
- Torque split between axles
- Optional locking mechanism

## Differential Covers

**Top Cover Part:** Center_diff_top_cover.SLDPRT  
**Material:** Polycarbonate  
**Weight:** ~15g

**Bottom Cover Part:** Center_diff_bottom.SLDPRT  
**Material:** Aluminum  
**Weight:** ~20g

Features:
- Dust sealing
- Easy access for maintenance
- Oil containment
- Bearing support

## Motor Mount System

**Part Number:** Motor_support_mount_1.SLDPRT / Motor_support_mount_2.SLDPRT / Motor_support_mount_3.SLDPRT  
**Material:** Aluminum  
**Weight:** ~35g (total)

### Mount Configuration
- 3-point adjustable system
- Allows pinion gear adjustment
- Supports motor load
- Vibration damping

### Alignment Procedure
1. Loosen all motor mount bolts
2. Position motor for smooth mesh
3. Check pinion-to-ring clearance (0.5mm)
4. Tighten progressively
5. Test rotation for binding

## Transmission Adapter

**Part Number:** Transmission_Adapter.SLDPRT  
**Material:** Steel  
**Weight:** ~25g

### Features
- Motor shaft to differential coupling
- Secure fastening
- Flexible design
- Standard flanges

### Connection Specifications
- Motor flange: 6mm
- Differential input: 6mm
- Bolts: M3 × 3 (4 total)
- Torque: 1.5-2.0 Nm

## Motor Specifications

**Type:** Brushless (3S/4S LiPo)  
**Specification:** 4000 KV  
**Power Output:** 2000W peak  
**Weight:** ~140g

### Motor Performance Data

| Parameter | Specification |
|-----------|----------------|
| Voltage Range | 9.6V - 14.8V |
| Max Current | 150A (with ESC) |
| Max RPM | 60,000 |
| Torque | 0.32 Nm per A |
| Efficiency | 85-90% |

### Cooling
- Direct wind airflow
- Optional fan shroud
- Temperature sensor recommended
- Max safe temp: 80°C continuous

## Axle Drive System

### Front Axle
- Input from differential front output
- Connects to front wheels
- CV joints at each end
- Length: 240mm

### Rear Axle
- Input from differential rear output
- Connects to rear wheels
- CV joints at each end
- Length: 240mm

### Axle Specifications

| Specification | Value |
|---------------|-------|
| Material | Steel with CV boots |
| Max RPM | 4000 |
| Max Torque | 25 Nm |
| Joint Type | Constant velocity |
| Maintenance | Grease every 3 months |

## Wheel & Tire System

**Wheel Part:** Wheel.SLDPRT  
**Tire Part:** Tire.SLDPRT

### Wheel Specifications
- Diameter: 80mm
- Width: 45mm
- Material: Aluminum alloy
- Mounting: M4 bolts (4 per wheel)
- Weight: ~18g per wheel

### Tire Specifications
- Type: Off-road compound
- Diameter: 80mm
- Width: 50mm
- Tread pattern: Optimized grip
- Material: Rubber compound
- Weight: ~25g per tire

### Tire Selection Guide

| Terrain | Tire Type | Tread | Grip |
|---------|-----------|-------|------|
| Asphalt | Slick | Minimal | High |
| Dirt | Knobby | Deep | Medium |
| Grass | Medium | Medium | Good |
| Mixed | All-terrain | Balanced | Balanced |

## Performance Ratios

### Gear Ratios
- Differential: 3.73:1
- Motor KV: 4000
- Max speed: ~50 km/h (estimated)
- Acceleration: 0-50 km/h in 2.5s

### Power Distribution
- Front axle: 50% power
- Rear axle: 50% power
- Adjustable with limited-slip diff

## Maintenance Schedule

### After Each Run
- [ ] Inspect for debris
- [ ] Check for oil leaks
- [ ] Listen for grinding noises
- [ ] Verify wheel tightness

### Weekly
- [ ] Differential oil check
- [ ] Axle boot inspection
- [ ] Motor temperature test
- [ ] Wheel bearing play check

### Monthly
- [ ] Oil change (if dirty)
- [ ] Deep clean drivetrain
- [ ] Bearing grease refresh
- [ ] Full system inspection

### Quarterly
- [ ] Gear mesh inspection
- [ ] Axle joint service
- [ ] Suspension lubrication
- [ ] Electronic system check

## Troubleshooting

| Symptom | Cause | Solution |
|---------|-------|----------|
| Grinding noise | Dirty oil | Change oil, flush system |
| Loss of traction | Worn tires | Replace tire set |
| Vibration | Wheel imbalance | Balance wheels |
| Slow acceleration | Low motor power | Check battery, ESC settings |
| Overheating | Poor airflow | Clean cooling vents |

## Upgrades & Modifications

### High-Performance Upgrades
- **Limited-Slip Diff** (+$40): Better traction
- **Ceramic Bearings** (+$20): Reduced friction
- **Braided Axles** (+$15): Increased strength
- **Performance Gears** (+$35): Better efficiency

### Tuning Options
- Adjust pinion gear teeth (15-19 tooth)
- Change motor KV (3000-5000 available)
- Modify gear ratio via diff
- Upgrade to brushless motor

## Related Systems

- [Motor & Electronics](electronics.md)
- [Chassis](chassis.md)
- [Suspension](suspension.md)
- [Wheels & Steering](steering.md)

---

**Component Version:** 1.0  
**Last Updated:** 2026-07-05
