from .base import BaseProvider


class YouTubeProvider(BaseProvider):

    def __init__(self, http):
        self.http = http

    async def search(self, query: str):

        return []
