import cadquery as cq

(L, H, W, t) = (100.0, 20.0, 20.0, 1.0)

pts = [
    (0, H / 2.0),
    (W / 2.0, H / 2.0),
    (W / 2.0, (H / 2.0 - t)),
    (t / 2.0, (H / 2.0 - t)),
    (t / 2.0, (t - H / 2.0)),
    (W / 2.0, (t - H / 2.0)),
    (W / 2.0, H / -2.0),
    (0, H / -2.0),
]

res = (
    cq.Workplane("front")
    .polyline(pts)
    .mirrorY()
    .extrude(L)
)

res.export("IMG_result.svg")

