from build123d import Compound, ExportSVG, LineType

def export_to_svg(part, filename="IMG_part.svg"):
    #view_port_origin = (-100, -50, 30)
    view_port_origin = (75, 50, 30)
    visible, hidden = part.project_to_viewport(view_port_origin)
    max_dimension = max(*Compound(children=visible + hidden).bounding_box().size)
    #
    exporter = ExportSVG(scale=100 / max_dimension, margin=5)
    exporter.add_layer("Visible")
    exporter.add_layer("Hidden", line_color=(99, 99, 99), line_type=LineType.ISO_DOT)
    exporter.add_shape(visible, layer="Visible")
    exporter.add_shape(hidden, layer="Hidden")
    exporter.write(filename)
    #
    return