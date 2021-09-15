import os
import json
from typing import *

import config


class Track:

    def __init__(self, title: str, lyrics: str) -> None:
        self.title = title
        self.lyrics = lyrics

    def to_json(self):
        """Allows to JSON serialize this class instances."""
        return json.dumps(self.__dict__)


class Album:

    def __init__(self, title: str, cover_url: str, tracks: List[Track]) -> None:
        self.title = title
        self.cover_url = cover_url
        self.tracks = tracks

    def to_json(self):
        """Allows to JSON serialize this class instances."""
        return json.dumps(self.__dict__)


class Artist:

    def __init__(self, name: str, image_url: str, albums: List[Album]) -> None:
        self.name = name
        self.path = os.path.join(config.DATA_DIR, f"{self.name.lower().replace(' ', '_')}.json")
        self.image_url = image_url
        self.albums = albums

    def save(self):
        """Saves instance of this class to JSON file."""
        with open(self.path, "w") as file:
            json.dump(self.__dict__, file, cls=ArtistEncoder)


class ArtistEncoder(json.JSONEncoder):
    """Class that allows JSON encoding of Artist class."""
    def default(self, o):
        return o.__dict__
