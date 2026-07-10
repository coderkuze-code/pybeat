from .client import Client
from .exceptions import (
    AuthenticationError,
    HTTPError,
    InvalidQuery,
    ProviderError,
    PyBeatError,
    SearchError,
    TrackNotFound,
    UnsupportedProvider,
)
from .models import (
    Album,
    Artist,
    Playlist,
    SearchResult,
    Track,
)
from .version import (
    __author__,
    __description__,
    __license__,
    __title__,
    __version__,
)

__all__ = (
    "Client",
    "Album",
    "Artist",
    "Playlist",
    "SearchResult",
    "Track",
    "PyBeatError",
    "ProviderError",
    "HTTPError",
    "AuthenticationError",
    "SearchError",
    "TrackNotFound",
    "UnsupportedProvider",
    "InvalidQuery",
    "__title__",
    "__description__",
    "__version__",
    "__author__",
    "__license__",
)
