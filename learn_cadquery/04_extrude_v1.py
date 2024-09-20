import cadquery as cq

res = (
    cq.Workplane("front")
    .circle(2.0)
    .rect(0.5, 0.75)
    .extrude(0.5)
)

res.export("IMG_result.svg")

