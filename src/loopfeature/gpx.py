def save_gpx(point_list:list[float, float], filename:str, path_dir:str):
    text_GPX = """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="LoopFeature" xmlns="http://www.topografix.com/GPX/1/1">
<trk>
<trkseg>"""
    
    for point in point_list:
        text_GPX += f'<trkpt lat="{point.latitude}" lon="{point.longitude}"><ele>{point.elevation}</ele></trkpt>\n'

    text_GPX += "</trkseg>\n</trk>\n</gpx>\n"
    
    filename = filename + ".gpx"
    path = path_dir / filename

    with open(path, "w") as file:
        file.write(text_GPX)