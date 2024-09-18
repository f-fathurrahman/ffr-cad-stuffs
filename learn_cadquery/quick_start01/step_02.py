import cadquery as cq

# unit in mm
height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0

# Make the base
result = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
)
# show_object(result)

# cadquery.Workplane.faces() selects the top-most face in the Z direction, and
# then cadquery.Workplane.workplane() begins a new workplane located on this face.
# The center of this workplane is located at the center of mass of the shape,
# which in this case is the center of the plate.
# Finally, cadquery.Workplane.hole() drills a hole through the part, 22mm in diameter.


result.export("IMG_step02.svg")

