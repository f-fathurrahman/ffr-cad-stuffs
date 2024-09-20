import cadquery as cq

length = 80.0
height = 60.0
thickness = 10.0

result = (
    cq.Workplane("YZ")
    .box(length, height, thickness)
)
# Meaning of length, height and thickness depends on Workplane type
# In the case of YZ workplane, length is the size of Y, height is size of Z,
# and thickness is size of X

result.export("IMG_result.svg")

