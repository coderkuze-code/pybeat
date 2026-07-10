from __future__ import annotations

from abc import ABC, abstractmethod

from pybeat.models import Track


class BaseProvider(ABC):

    name: str = "BaseProvider"

    def __init__(self, client=None):
        self.client = client

    @abstractmethod
    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Track]:

        raise NotImplementedError

    async def get_track(
        self,
        track_id: str,
    ) -> Track:

        raise NotImplementedError(
            f"{self.name} doesn't support get_track()."
        )

    async def get_playlist(
        self,
        playlist_id: str,
    ):

        raise NotImplementedError(
            f"{self.name} doesn't support playlists."
        )

    async def get_album(
        self,
        album_id: str,
    ):

        raise NotImplementedError(
            f"{self.name} doesn't support albums."
        )

    async def get_artist(
        self,
        artist_id: str,
    ):

        raise NotImplementedError(
            f"{self.name} doesn't support artists."
        )

    async def stream(
        self,
        track: Track,
    ) -> str:
        
        raise NotImplementedError(
            f"{self.name} doesn't support streaming."
        )

    async def lyrics(
        self,
        track: Track,
    ) -> str:

        raise NotImplementedError(
            f"{self.name} doesn't support lyrics."
        )

    async def close(self):

        return None
