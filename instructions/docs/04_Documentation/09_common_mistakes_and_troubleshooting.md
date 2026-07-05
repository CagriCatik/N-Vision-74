# 09 - Common Mistakes and Troubleshooting

!!! failure "Mistake 1: Modelling the whole car as one part"
    Problem:

    - difficult to print,
    - difficult to repair,
    - poor support placement,
    - large failed prints,
    - hard to revise.

    Better:

    - split body, chassis, wheels, and details into separate parts,
    - use an assembly file,
    - add alignment features.

!!! failure "Mistake 2: Tracing blueprint lines too literally"
    Problem:

    - online blueprints are often distorted,
    - views may not match,
    - curves become messy,
    - surface features fail.

    Better:

    - use real dimensions,
    - trace only important curves,
    - rebuild clean splines,
    - verify from multiple views.

!!! failure "Mistake 3: Too many spline points"
    Problem:

    - wavy surfaces,
    - unstable lofts,
    - bad curvature,
    - hard editing.

    Better:

    - use fewer points,
    - use curvature combs,
    - use guide curves,
    - split complex surfaces into patches.

!!! failure "Mistake 4: Thin cosmetic parts"
    Problem:

    - mirrors break,
    - panel lines disappear,
    - grilles fail,
    - door handles are not printable.

    Better:

    - exaggerate tiny details slightly,
    - print small details separately,
    - use resin for fine details if needed,
    - test print details before final body.

!!! failure "Mistake 5: No assembly clearance"
    Problem:

    - parts do not fit,
    - pins jam,
    - screw holes are too tight,
    - paint makes fit worse.

    Better:

    - add 0.3-0.5 mm clearance for normal FDM assembly,
    - leave extra clearance for painted parts,
    - use tolerance coupons.

!!! failure "Mistake 6: Surface model cannot be thickened"
    Possible causes:

    - tight curvature smaller than wall thickness,
    - self-intersecting thicken direction,
    - open surface gaps,
    - twisted lofts,
    - bad patch boundaries.

    Fix:

    1. Reduce thicken value temporarily.
    2. Inspect open edges.
    3. Rebuild problematic surface patch.
    4. Add fillets after thickening where possible.
    5. Use multiple smaller thickened bodies if needed.

!!! failure "Mistake 7: Exterior surface damaged by supports"
    Problem:

    - support scars on roof, bonnet, or side panels,
    - heavy sanding required,
    - surface accuracy lost.

    Better:

    - split the part differently,
    - orient visible surface away from support contact,
    - place supports on inner surfaces,
    - print bumper and body sections separately.

!!! failure "Mistake 8: Ignoring post-processing"
    Problem:

    - paint makes joints too tight,
    - sanding removes panel lines,
    - glue joints are too small,
    - filler hides fine details.

    Better:

    - design deeper panel lines,
    - include paint clearance,
    - add hidden bonding flanges,
    - separate delicate details.

!!! bug "Troubleshooting: Loft fails"
    Check:

    - profiles are selected in consistent order,
    - guide curves intersect all profiles,
    - profiles are not self-intersecting,
    - guide curves are not crossing unexpectedly,
    - start/end constraints are appropriate.

!!! bug "Troubleshooting: Boundary surface twists"
    Check:

    - Direction 1 and Direction 2 curves are logically arranged,
    - curves meet at corners,
    - connector handles are aligned,
    - profiles are not reversed,
    - patch is too large and should be divided.

!!! bug "Troubleshooting: STL is wrong scale"
    Check:

    - SolidWorks units are millimetres,
    - export units are millimetres,
    - slicer import unit is millimetres,
    - no accidental inch conversion occurred.

!!! bug "Troubleshooting: printed holes are too small"
    Fix:

    - increase hole diameter by 0.2-0.4 mm,
    - print hole test coupon,
    - drill after printing,
    - use heat-set inserts for threaded holes.
