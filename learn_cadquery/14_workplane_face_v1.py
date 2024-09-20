import cadquery as cq

"""
The Workplane.faces() method allows you to select the faces of a resulting solid.
It accepts a selector string or object, that allows you to target a single face,
and make a workplane oriented on that face.

Keep in mind that by default the origin of a new workplane is calculated by
forming a plane from the selected face and projecting the previous origin onto
that plane. This behaviour can be changed through the centerOption argument
of Workplane.workplane().
"""

res = cq.Workplane("front").box(2, 3, 0.5)  # make a basic prism

res = (
    res.faces(">Z").workplane().hole(0.5)
)  # find the top-most face and make a hole