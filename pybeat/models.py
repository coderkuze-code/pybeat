from dataclasses import dataclass


@dataclass(slots=True)
class Track:
    id: str
    title: str
    artist: str
    duration: int
    thumbnail: str
    source: str
