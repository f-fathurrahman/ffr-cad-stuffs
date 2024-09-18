"""
Ok, that hole was not too hard, but what about the counter-bored holes in the corners?
An M2 Socket head cap screw has these dimensions:
• Head Diameter : 3.8 mm
• Head height : 2.0 mm
• Clearance Hole : 2.4 mm
• CounterBore diameter : 4.4 mm
The centers of these holes should be 6mm from the edges of the block. And, we want the block to work correctly even
when the block is re-sized by the user.
Don't tell me we’ll have to repeat the steps above 8 times to get counter-bored holes? Good news!– we can get the job
done with just a few lines of code. Here’s the code we need:
"""

import cadquery as cq


# unit in mm
height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0

# Make the base
result = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
    .faces(">Z")
    .workplane()
    .rect(height-padding, width-padding, forConstruction=True)
    .vertices()
    .cboreHole(2.4, 4.4, 2.1)
)

result.export("IMG_step03.svg")

