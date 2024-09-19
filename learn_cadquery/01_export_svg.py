import cadquery as cq
from cadquery import exporters

result = cq.Workplane().box(10, 10, 10)
opt = {
    "width": 300,
    "height": 300,
    "marginLeft": 10,
    "marginTop": 10,
    "showAxes": False,
    "projectionDir": (0.5, 0.5, 0.5),
    "strokeWidth": 0.25,
    "strokeColor": (255, 0, 0),
    "hiddenColor": (0, 0, 255),
    "showHidden": True,
}
result.export("IMG_01_box.svg", opt=opt)



