import cadquery as cq

# unit in mm
height = 60.0
width = 80.0
thickness = 10.0

result = cq.Workplane("XY").box(height, width, thickness)
# show_object(result)

result.export("IMG_step01.svg")

