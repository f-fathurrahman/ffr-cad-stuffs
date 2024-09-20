import cadquery as cq

res = (
    cq.Workplane("front")
    .box(3.0, 4.0, 0.25)
    .pushPoints([( 0,0.75 ), (0, -0.75)])
    .polygon(6, 1.0)
    .cutThruAll()
)
res.export("IMG_result.svg")
