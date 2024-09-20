import cadquery as cq

res = (
    cq.Workplane("XY")
    .line(0, 1)
    .line(1, 0)
    .line(0, -0.5)
    .close()
    .extrude(1)
)
res = res.mirror(res.faces(">X"), union=True)
res.export("IMG_result.svg")
