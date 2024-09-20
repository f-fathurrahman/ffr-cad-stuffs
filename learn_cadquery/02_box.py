import cadquery as cq

def my_export_svg(r):
    r.export("IMG_result.svg",
        opt = {
            #"width": 300,
            #"height": 300,
            #"marginLeft": 10,
            #"marginTop": 10,
            #"showAxes": True,
            #"projectionDir": (0.5, 0.5, 0.5),
            #"strokeWidth": 0.25,
            #"strokeColor": (0, 0, 0),
            #"hiddenColor": (0, 0, 255),
            #"showHidden": True,
        }
    )
    return


result = cq.Workplane("front").box(5, 4, 1.0)
my_export_svg(result)



