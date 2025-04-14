from build123d import *
from my_utils import export_to_svg

length, width, thickness = 80.0, 60.0, 10.0
center_hole_dia = 22.0

with BuildPart() as ex2:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)

export_to_svg(ex2.part, filename="IMG_02.svg")
export_step(ex2.part, "IMG_02.step")


