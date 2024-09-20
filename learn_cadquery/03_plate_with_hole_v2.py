import cadquery as cq

length = 80.0
height = 60.0
thickness = 50.0
center_hole_dia = 22.0

result = (
    cq.Workplane("XZ")
    .box(length, height, thickness)
    .faces(">X")
    .workplane()
    .hole(center_hole_dia)
)

result.export("IMG_result.svg")

