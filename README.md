# LoopFeature

LoopFeature is a Python project that automatically generates trail running loops from a chosen starting point and target distance.

The objective is not only to generate a route, but to build an enjoyable trail loop by favouring paths with elevation gain, natural surfaces and interesting terrain while always returning to the starting point.

> **Project status:** Work in progress 🚧

---

## Features

- Generate a loop from GPS coordinates
- User-defined target distance
- Automatic return to the starting point
- Uses OpenStreetMap data through the Overpass API
- Elevation extracted locally from Copernicus DEM raster files
- GPX export compatible with Strava, Garmin, Komoot and most GPS devices
- Graph-based route generation
- Segment scoring system based on trail-oriented criteria

---

## How it works

The application follows several steps:

1. Download walkable paths from OpenStreetMap using the Overpass API.
2. Build a graph where:
   - vertices represent OSM points,
   - edges represent path segments.
3. Read elevation from a local DEM (Copernicus).
4. Compute characteristics for every segment:
   - distance,
   - elevation gain,
   - surface,
   - road type,
   - custom score.
5. Generate a loop using a heuristic algorithm that attempts to maximize route quality while respecting the requested distance.
6. Export the final route as a GPX file.

---

## Technologies

- Python
- OpenStreetMap
- Overpass API
- Rasterio
- Copernicus DEM
- GPX 1.1

---

## Current scoring criteria

The route generation algorithm currently considers several factors:

- trail type (`path`, `footway`, `track`, ...)
- surface quality
- estimated elevation gain
- segment length
- distance from the starting point
- already visited vertices
- already travelled edges
- quality of neighbouring segments

The scoring function is still under active development.

---

## Roadmap

Planned improvements include:

- Better optimisation algorithm
- More realistic elevation modelling
- Better loop quality
- Configurable user preferences

---

## Install

Install it with pip:
```python
pip install git+https://github.com/FleterEwenn/LoopFeature.git#egg=loopfeature
```

To use it, just import it as module:
```python
import loopfeature
```
Or:
```python
from loopfeature import generate_route, save_gpx
```

## Testing

Unit tests are written using **pytest**.

Run them with:

```bash
python -m pytest
```

---

## Why this project?

LoopFeature started as a personal project to learn:

- graph theory
- shortest path algorithms (Dijkstra)
- OpenStreetMap data
- geographic computations
- DEM processing
- object-oriented programming
- software architecture
- testing with pytest

The long-term goal is to build a real trail route planner able to generate enjoyable loops automatically.
