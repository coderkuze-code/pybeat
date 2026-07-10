from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def search(self, query: str):
        raise NotImplementedError
