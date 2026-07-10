from __future__ import annotations
import re
from urllib.parse import parse_qs, urlparse


YOUTUBE_VIDEO_ID = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/))([A-Za-z0-9_-]{11})"
)


def clean_query(query: str) -> str:

    return " ".join(query.strip().split())


def is_url(text: str) -> bool:

    parsed = urlparse(text)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def parse_duration(duration: str) -> int:

    parts = [int(x) for x in duration.split(":")]

    if len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds

    if len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds

    raise ValueError("Invalid duration format")


def format_duration(seconds: int) -> str:

    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)

    if h:
        return f"{h:02}:{m:02}:{s:02}"

    return f"{m:02}:{s:02}"


def extract_youtube_video_id(url: str) -> str | None:

    if "youtu.be" in url:
        return url.rstrip("/").split("/")[-1]

    parsed = urlparse(url)

    if parsed.hostname and "youtube.com" in parsed.hostname:
        query = parse_qs(parsed.query)

        if "v" in query:
            return query["v"][0]

    match = YOUTUBE_VIDEO_ID.search(url)

    if match:
        return match.group(1)

    return None
