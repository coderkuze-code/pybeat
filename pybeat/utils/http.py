import httpx


class HTTPClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            timeout=30,
            follow_redirects=True,
            headers={
                "User-Agent": "PyBeat/0.0.1"
            }
        )

    async def get(self, url: str, **kwargs):
        response = await self.client.get(url, **kwargs)
        response.raise_for_status()
        return response

    async def post(self, url: str, **kwargs):
        response = await self.client.post(url, **kwargs)
        response.raise_for_status()
        return response

    async def close(self):
        await self.client.aclose()
