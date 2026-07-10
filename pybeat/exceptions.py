class PyBeatError(Exception):

class ProviderError(PyBeatError):

class HTTPError(PyBeatError):

class AuthenticationError(PyBeatError):

class SearchError(PyBeatError):

class TrackNotFound(PyBeatError):

class UnsupportedProvider(PyBeatError):

class InvalidQuery(PyBeatError):
