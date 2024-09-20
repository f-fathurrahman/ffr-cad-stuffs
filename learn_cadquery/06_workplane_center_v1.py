import cadquery as cq

res = cq.Workplane("front").circle(3.0)
# current point is the center of the circle, at (0, 0)

res = res.center(1.5, 0.0).rect(0.5, 0.5)
# new work center is (1.5, 0.0)

res = res.center(-1.5, 1.5).circle(0.25)  # new work center is (0.0, 1.5).
# The new center is specified relative to the previous center, not global coordinates!

# move the center again, using relative coord
res = res.center(-1.5, -1.5).circle(0.3)
res = res.center(1.5, -1.5).rect(0.3, 0.3)

res = res.extrude(0.75)

res.export("IMG_result.svg")