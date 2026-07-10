from .providers.youtube import YouTubeProvider


class Client:
    def __init__(self):
        self.providers = [
            YouTubeProvider()
        ]

    async def search(self, query: str):
        results = []

        for provider in self.providers:
            try:
                results.extend(await provider.search(query))
            except Exception:
                continue

        return results
