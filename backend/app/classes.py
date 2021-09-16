import os
import json
from typing import *

import config


class Track:
    """
    Class representation of single music track.
    """

    def __init__(self, title: str, lyrics: str) -> None:
        self.title = title
        self.lyrics = lyrics

    def to_json(self):
        """Allows to JSON serialize this class instances."""
        return json.dumps(self.__dict__)


class Album:
    """
    Class representation of single music album.
    """

    def __init__(self, title: str, cover_url: str, tracks: List[Track]) -> None:
        self.title = title
        self.cover_url = cover_url
        self.tracks = tracks

    def to_json(self):
        """Allows to JSON serialize this class instances."""
        return json.dumps(self.__dict__)


class Artist:
    """
    Class representation of single music artist.
    """

    def __init__(self, name: str, image_url: str, albums: List[Album]) -> None:
        self.name = name
        self.path = os.path.join(config.DATA_DIR, f"{self.name.lower().replace(' ', '_')}.json")
        self.image_url = image_url
        self.albums = albums

    @classmethod
    def load(cls, json_dict: dict):
        """Creates instance of this class, base on JSON file content."""
        # dictionary that stores creation parameters
        parameters = {
            "name": json_dict.get("name"),
            "image_url": json_dict.get("image_url"),
            "albums": []
        }
        # iteration over albums in JSON file and collecting Albums objects
        for album in json_dict["albums"]:
            # iteration over tracks in current album and collecting Tracks obejcts
            tracks = []
            for track in album["tracks"]:
                tracks.append(Track(title=track.get("title"), lyrics=track.get("lyrics")))
            # appending Album object to list
            parameters["albums"].append(
                Album(title=album.get("title"), cover_url=album.get("cover_url"), tracks=tracks)
            )
        # creates class instance base on collected parameters
        return cls(**parameters)

    def save(self):
        """Saves instance of this class to JSON file."""
        with open(self.path, "w") as file:
            json.dump(self.__dict__, file, cls=ArtistEncoder)


class ArtistEncoder(json.JSONEncoder):
    """Class that allows JSON encoding of Artist class."""
    def default(self, o):
        return o.__dict__
