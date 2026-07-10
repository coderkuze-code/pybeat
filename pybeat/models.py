from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class Artist(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Optional[str] = None
    name: str
    url: Optional[HttpUrl] = None


class Album(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Optional[str] = None
    title: str
    artist: Optional[str] = None
    cover: Optional[HttpUrl] = None
    year: Optional[int] = None


class Track(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    title: str
    artist: Artist

    album: Optional[Album] = None

    duration: Optional[int] = None

    source: str

    url: Optional[HttpUrl] = None

    thumbnail: Optional[HttpUrl] = None

    is_explicit: bool = False


class Playlist(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: Optional[str] = None

    title: str

    creator: Optional[str] = None

    tracks: list[Track] = []


class SearchResult(BaseModel):
    model_config = ConfigDict(frozen=True)

    query: str

    provider: str

    tracks: list[Track]
