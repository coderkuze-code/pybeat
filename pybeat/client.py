from .utils.http import HTTPClient
from .providers.youtube import YouTubeProvider


class Client:

    def __init__(self):
        self.http = HTTPClient()

        self.providers = [
            YouTubeProvider(self.http)
        ]

    async def search(self, query: str):
        results = []

        for provider in self.providers:
            try:
                results.extend(await provider.search(query))
            except Exception:
                pass

        return results

    async def close(self):
        await self.http.close()
