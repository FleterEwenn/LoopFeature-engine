def generate_GPX(point_list:list[float, float]):
    text_GPX = "<xml>\n<gpx>\n<trk>\n<trkseg>\n"
    for point in point_list:
        text_GPX += " <trkpt lat={point[0]} lon={point[1]}></trkpt>"
    text_GPX += "</trkseg>\n</trk>\n</gpx>\n</xml>\n"
    with open("trace.gpx", "r") as file:
        file.write(text_GPX)

generate_GPX([(45.02946, 1.78383), (45.0294, 1.78386), (45.02946, 1.78383), (45.0294, 1.78386), (45.02946, 1.78383), (45.0294, 1.78386), (45.02946, 1.78383), (45.0294, 1.78386), (45.02916, 1.78398), (45.0294, 1.78386), (45.02946, 1.78383)])
