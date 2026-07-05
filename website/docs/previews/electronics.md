# Electronics Components

Interactive 3D preview of the N-Vision-74 electronics and electrical system.

## Overview

The electronics system provides power, motor control, steering control, and system management.

## ESC (Electronic Speed Controller)

**Specification:** 150A Brushless ESC  
**Voltage:** 3S/4S LiPo (9.6V - 14.8V)  
**Dimensions:** 75mm × 35mm × 25mm  
**Weight:** ~35g

### Features
- Brushless motor support
- Programmable parameters
- Thermal protection
- Waterproof rating (IP67)
- BEC (Battery Elimination Circuit)
- LED indicator lights

### Specifications Table

| Parameter | Value |
|-----------|-------|
| Max Current | 150A peak |
| Continuous Current | 120A |
| BEC Output | 6V @ 5A |
| Frequency | 32kHz PWM |
| Programming | Bluetooth enabled |
| Thermal Shutdown | 75°C |

### ESC Functions
1. **Motor Control** - Speed regulation via throttle
2. **Brake Control** - Regenerative braking
3. **Direction Control** - Forward and reverse
4. **Power Distribution** - BEC to receiver
5. **Protection** - Temperature and voltage monitoring

## Brushless Motor

**Type:** Sensored Brushless  
**KV Rating:** 4000  
**Voltage:** 3S/4S LiPo  
**Dimensions:** 35mm × 42mm diameter  
**Weight:** ~140g

### Motor Specifications

| Specification | Value |
|---------------|-------|
| Max RPM | 60,000 |
| Power Output | 2000W peak |
| Torque | 0.32 Nm per amp |
| Current (no load) | 2A @ 12V |
| Efficiency | 85-90% |
| Mounting | 4 × M3 bolts |

### Cooling System
- Direct airflow design
- Optional fan shroud
- Temperature sensor (optional)
- Maximum safe temperature: 80°C

### Motor Mounting
1. Position motor on mounts
2. Align pinion with ring gear
3. Check clearance (0.5mm)
4. Tighten progressively
5. Test rotation smoothly

## Servo (Steering Control)

**Type:** Digital Standard Servo  
**Torque:** 8 kg·cm  
**Speed:** 0.18s per 60°  
**Voltage:** 4.8V - 6.0V  
**Weight:** ~40g

### Servo Specifications

| Parameter | Value |
|-----------|-------|
| Operating Voltage | 4.8V - 6.0V |
| Operating Current | 50mA idle, 800mA active |
| Torque | 8 kg·cm @ 4.8V, 10 kg·cm @ 6.0V |
| Speed | 0.18s/60° @ 4.8V |
| Dead Band | 2μs |
| Gear Type | Plastic with metal output |
| Mounting | Standard servo bracket |

### Servo Functions
1. Steering control input from receiver
2. Translation to wheel angle
3. Position feedback
4. Centering mechanism
5. End point adjustment

### Installation
1. Mount servo to bracket
2. Attach servo arm
3. Connect to receiver (Channel 1)
4. Calibrate center position
5. Test full range

## Battery System

**Type:** LiPo (Lithium Polymer)  
**Configuration:** 3S (3-cell) or 4S (4-cell)  
**Capacity:** 5000mAh recommended  
**C-Rating:** 100C discharge

### Battery Specifications

| Cell Count | Voltage | Capacity | Weight |
|-----------|---------|----------|--------|
| 3S LiPo | 11.1V nominal | 5000mAh | ~350g |
| 4S LiPo | 14.8V nominal | 5000mAh | ~450g |

### Performance Comparison

| Spec | 3S Battery | 4S Battery |
|------|-----------|-----------|
| Max Speed | 45 km/h | 55 km/h |
| Acceleration | Good | Excellent |
| Run Time | 20-30 min | 15-25 min |
| Motor Heat | Moderate | Higher |
| ESC Load | Lower | Higher |

### Battery Safety
- Always use LiPo charger
- Never overcharge (4.25V per cell max)
- Don't discharge below 3V per cell
- Store at 3.8V per cell (storage mode)
- Check for swelling/puffing
- Replace if damaged

### Charging Procedure
1. Connect balance plug to charger
2. Set voltage to battery type (3S or 4S)
3. Set charge rate to 1-2C (5000mAh = 5-10A)
4. Charge until complete
5. Unplug and allow to cool

## Battery Tray

**Part Number:** Battery_tray_L.SLDPRT / Battery_tray_R.SLDPRT  
**Material:** Plastic  
**Weight:** ~10g each  
**Mounting:** Chassis sides (L/R)

### Features
- Modular side mounting
- Strap hooks for battery retention
- Easy access for removal
- Symmetrical placement for balance

## Power Distribution System

**Input Voltage:** 14.8V max (4S LiPo)  
**Output:** 6V BEC @ 5A  
**Gold Connectors:** Low resistance  
**Fusing:** 150A main fuse

### Power Flow Diagram
```
Battery → ESC → Motor
       → BEC → Receiver/Servo
```

### Connection Specifications

| Connector | Wire | Gauge | Connections |
|-----------|------|-------|------------|
| Battery Main | 10AWG | 2mm² | XT90 |
| Motor Phase | 8AWG | 3mm² | 3.5mm bullet |
| BEC Output | 18AWG | 0.8mm² | Servo connector |
| ESC Signal | 22AWG | 0.3mm² | Three-pin header |

## ESC Box Enclosure

**Part Number:** Ele_box_body_ESC.SLDPRT  
**Material:** Polycarbonate  
**Weight:** ~45g  
**Waterproof:** IP67 rated

### Features
- Weatherproof housing
- Efficient heatsinking
- Easy access panels
- Cable management ports
- Ventilation slots

### ESC Installation
1. Position ESC in box
2. Route motor wires through port
3. Route battery wires separately
4. Secure with foam padding
5. Close enclosure

## Cooling System

**Fan Shroud:** Ele_cover.SLDPRT  
**Material:** Plastic  
**Function:** Direct motor airflow  
**Weight:** ~12g

### Cooling Management
1. Direct wind airflow over motor
2. Shroud guides air efficiently
3. Ventilation holes in body
4. Optional active cooling fan

### Thermal Monitoring
- Visual temperature indicator
- ESC thermal shutdown (75°C)
- Motor thermistor (optional)
- Recommended limit: 70°C

## Receiver & Transmitter System

**Type:** 2.4GHz FHSS  
**Channels:** 6+ channels  
**Range:** 300m+ line-of-sight

### Receiver Specifications

| Parameter | Value |
|-----------|-------|
| Frequency | 2.4GHz |
| Modulation | FHSS hopping |
| Channels | 6+ |
| Servo Frequency | 50Hz standard |
| Failsafe | Programmable |
| Weight | ~15g |

### Transmitter Features
- Proportional throttle control
- Proportional steering control
- Trim adjustment
- Model memory (4+ models)
- Battery level indicator

## Wiring Diagram

```
[Battery LiPo]
      |
      ├→ [ESC Main Input]
      |      |
      |      ├→ [Motor Phase Wires]
      |      |
      |      └→ [BEC 6V Output]
      |             |
      |             ├→ [Receiver Power]
      |             |
      |             └→ [Servo Power]
      |
[Receiver]
      |
      ├→ [Servo Signal] → [Steering Servo]
      |
      └→ [Throttle Signal] → [ESC Control]
```

## Maintenance & Safety

### Daily Checks
- Battery voltage before run
- Connection security
- Motor spin freely
- Servo movement smooth

### Weekly Maintenance
- Check for corrosion
- Verify all connections tight
- Test failsafe function
- Inspect for water damage

### Monthly Service
- Clean all connectors
- Inspect wiring insulation
- Update ESC firmware
- Calibrate steering center

## Electronics Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| No power | Dead battery | Charge battery |
| Motor won't spin | ESC issue | Reset/reprogram |
| Servo stuttering | Low battery | Charge battery |
| No steering | Servo disconnected | Check connection |
| Overheating | Poor airflow | Clean vents |

## Safety Warnings

⚠️ **High Voltage** - 4S LiPo can deliver 150A current  
⚠️ **LiPo Fire Risk** - Never short battery terminals  
⚠️ **Hot Components** - Motor and ESC get very hot  
⚠️ **Propeller Hazard** - Keep hands clear during testing  

## Related Components

- [Motor & Drivetrain](drivetrain.md)
- [Steering System](steering.md)
- [Battery & Charging Guide](../getting_started/bom.md)

---

**Component Version:** 1.0  
**Last Updated:** 2026-07-05
