from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    latitude:float
    longitude:float