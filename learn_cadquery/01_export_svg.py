import cadquery as cq
from cadquery import exporters

result = cq.Workplane().box(10, 10, 10)
result.export("IMG_01_box.svg")

