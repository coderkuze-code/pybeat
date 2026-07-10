from __future__ import annotations
from typing import Any
import httpx
from pybeat.exceptions import HTTPError


class HTTPClient:
    
    def __init__(
        self,
        *,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
        proxy: str | None = None,
    ) -> None:

        self._client = httpx.AsyncClient(
            timeout=timeout,
            headers=headers
            or {
                "User-Agent": "PyBeat/0.0.1",
                "Accept": "*/*",
            },
            proxy=proxy,
            follow_redirects=True,
            http2=True,
        )

    async def get(
        self,
        url: str,
        **kwargs: Any,
    ) -> httpx.Response:
        try:
            response = await self._client.get(
                url,
                **kwargs,
            )
            response.raise_for_status()
            return response

        except httpx.HTTPError as e:
            raise HTTPError(str(e)) from e

    async def post(
        self,
        url: str,
        **kwargs: Any,
    ) -> httpx.Response:
        try:
            response = await self._client.post(
                url,
                **kwargs,
            )
            response.raise_for_status()
            return response

        except httpx.HTTPError as e:
            raise HTTPError(str(e)) from e

    async def request(
        self,
        method: str,
        url: str,
        **kwargs: Any,
    ) -> httpx.Response:
        try:
            response = await self._client.request(
                method,
                url,
                **kwargs,
            )
            response.raise_for_status()
            return response

        except httpx.HTTPError as e:
            raise HTTPError(str(e)) from e

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ):
        await self.close()
