# PyBeat

> A modern, asynchronous Python media library.

PyBeat is a lightweight and extensible Python library that provides a unified API for searching and retrieving media from multiple providers such as YouTube, Spotify, SoundCloud, and more.

## Features

- ⚡ Fully asynchronous
- 🔌 Provider-based architecture
- 🎵 Unified media models
- 📜 Type hinted API
- 🚀 Fast HTTP client powered by httpx
- 🛠️ Easy to extend

## Installation

```bash
pip install pybeat
```

Or install the latest development version:

```bash
git clone https://github.com/your-org/pybeat.git
cd pybeat
pip install -e .
```

## Quick Start

```python
import asyncio

from pybeat import Client


async def main():
    client = Client()

    results = await client.search("Believer")

    for track in results:
        print(track.title)

    await client.close()


asyncio.run(main())
```

## Project Structure

```
pybeat/
├── client.py
├── models.py
├── providers/
├── utils/
└── exceptions.py
```

## Roadmap

- [x] Core package
- [ ] HTTP client
- [ ] YouTube provider
- [ ] Spotify provider
- [ ] SoundCloud provider
- [ ] Playlist support
- [ ] Lyrics API
- [ ] Streaming API
- [ ] Documentation
- [ ] PyPI release

## License

MIT License
