import cadquery as cq

# A common use case is to use a for-construction rectangle to
# define the centers of a hole pattern:

res = (
    cq.Workplane()
    .box(10, 10, 2)
    .workplane()
    .rect(4.0, 4.0, forConstruction=True)
    .vertices()
    .circle(0.25)
    .extrude(1.0)
)

res.export("IMG_result.svg")

