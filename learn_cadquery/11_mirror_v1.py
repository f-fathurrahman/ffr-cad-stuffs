import cadquery as cq

r = cq.Workplane("front").hLine(1.0)  # 1.0 is the distance, not coordinate
r = (
    r.vLine(0.5).hLine(-0.25).vLine(-0.25).hLineTo(0.0)
)  # hLineTo allows using xCoordinate not distance

res = r.mirrorY().extrude(0.25)  # mirror the geometry and extrude

res.export("IMG_result.svg")
