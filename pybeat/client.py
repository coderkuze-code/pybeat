from __future__ import annotations

from typing import Iterable

from .exceptions import InvalidQuery, ProviderError
from .models import Track


class Client:

    def __init__(self) -> None:
        self._providers = []

    @property
    def providers(self):
        return tuple(self._providers)

    def register(self, provider) -> None:

        if provider in self._providers:
            return

        self._providers.append(provider)

    def unregister(self, provider) -> None:

        if provider in self._providers:
            self._providers.remove(provider)

    async def search(
        self,
        query: str,
        limit: int = 10,
    ) -> list[Track]:

        if not query.strip():
            raise InvalidQuery("Query cannot be empty.")

        results = []

        for provider in self._providers:
            try:
                tracks = await provider.search(
                    query=query,
                    limit=limit,
                )

                if tracks:
                    results.extend(tracks)

            except Exception as e:
                raise ProviderError(
                    f"{provider.name}: {e}"
                ) from e

        return results[:limit]

    async def close(self):

        for provider in self._providers:
            close = getattr(provider, "close", None)

            if callable(close):
                await close()

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        exc_type,
        exc,
        tb,
    ):
        await self.close()
