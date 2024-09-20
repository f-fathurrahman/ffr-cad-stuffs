import cadquery as cq

res = cq.Workplane("front").box(3, 2, 0.5)  # make a basic prism

res = res.faces("<X").workplane(offset=0.75)
# workplane is offset from the object surface

res = res.circle(1.0).extrude(0.5)  # disc

res.export("IMG_result.svg")
