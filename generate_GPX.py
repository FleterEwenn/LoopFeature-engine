def generate_GPX(point_list:list[float, float]):
    text_GPX = "<xml>\n<gpx>\n<trk>\n<trkseg>\n"

    for point in point_list:
        text_GPX += f'<trkpt lat="{point[0]}" lon="{point[1]}"></trkpt>\n'

    text_GPX += "</trkseg>\n</trk>\n</gpx>\n</xml>\n"
    
    with open("trace.gpx", "w") as file:
        file.write(text_GPX)