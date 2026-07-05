import requests
import zipfile
import os
from pathlib import Path

parent = Path(__file__).parent

def get_tile(center:tuple[float, float])->str:
    lat = int((center[0]//10)*10)
    lon = int((center[1]//10)*10)

    filename = f"10_DEM_y{lat}x{lon}.tif"

    if os.path.exists(parent / "data" / filename):
        return filename 
    else:
        download_tile(lat, lon, filename)
        return filename

def download_tile(lat:int, lon:int, filename:str):
    url = f"https://gisco-services.ec.europa.eu/dem/copernicus/outD/10_DEM_y{lat}x{lon}.zip"
    response = requests.get(url)

    with open(parent / "archive.zip", "wb") as zip:
        zip.write(response.content)
    
    with zipfile.ZipFile(parent / "archive.zip", "r") as zip_ref:
        zip_ref.extract(filename, parent / "data")
    os.remove(parent / "archive.zip")