"""
This script contains classes definition of objects used in whole application.
"""


import json
import os
from typing import *

import config
from app.utills import FilesManager
from app.nlp import NLP


class Track:
    """Class representation of single music track."""

    def __init__(self, title: str, lyrics: str) -> None:
        """Creates instance of Track class.

        Args:
            title (str): track title.
            lyrics (str): track lyrics.
        """
        self.title = title
        self.lyrics = lyrics

    def __str__(self) -> str:
        """String representation of this classes instances."""
        return f"Title: {self.title}\nLyrics:{self.lyrics}"

    @property
    def lyrics_processed(self) -> str:
        """Using NLP class to process track lyrics."""
        return NLP.text_process(text=self.lyrics)


class Album:
    """Class representation of single music album."""

    def __init__(self, title: str, cover_url: str, tracks: List[Track]) -> None:
        """Creates instance of Album class.

        Args:
            title (str): album title.
            cover_url (str): URL adress to album cover.
            tracks (List[Track]): list of Track class objects.
        """
        self.title = title
        self.cover_url = cover_url
        self.tracks = tracks

    def __str__(self) -> str:
        """String representation of this classes instances."""
        return f"Title: {self.title}\nTracklist: {self.track_list}"

    @property
    def track_list(self) -> List[str]:
        """Returns list of tracks names."""
        return [track.title for track in self.tracks if track.title]

    @property
    def lyrics(self) -> str:
        """Returns string that contains lyrics of each tracks in album."""
        list_of_tracks_lyrics = [track.lyrics for track in self.tracks]
        album_lyrics = " ".join(list_of_tracks_lyrics)
        return album_lyrics

    @property
    def lyrics_processed(self) -> str:
        """Returns string that contains processed lyrics of each tracks in album."""
        list_of_tracks_lyrics = [track.lyrics_processed for track in self.tracks]
        album_lyrics = " ".join(list_of_tracks_lyrics)
        return album_lyrics


class Artist:
    """Class representation of single music artist."""

    def __init__(self, name: str, image_url: str, albums: List[Album]) -> None:
        """Creates instance of Artist class.

        Args:
            name (str): name of artist.
            image_url (str): URL adress to artist image.
            albums (List[Album]): list of Album class objects.
        """
        self.name = name
        self.image_url = image_url
        self.albums = albums
        # path to artist JSON file
        self.path = os.path.join(config.DATA_DIR, self.get_filename(name=name))

    def __str__(self) -> str:
        """String representation of this classes instances."""
        return f"Name: {self.name}\nAlbums: {self.album_list}"

    @property
    def album_list(self) -> List[str]:
        """Returns list of album names."""
        return [album.title for album in self.albums if album.title]

    @property
    def lyrics(self) -> str:
        """Returns string that contains lyrics of each tracks of each album."""
        list_of_album_lyrics = [album.lyrics for album in self.albums]
        artist_lyrics = " ".join(list_of_album_lyrics)
        return artist_lyrics

    @property
    def lyrics_processed(self) -> str:
        """Returns string that contains processed lyrics of each tracks of each album."""
        list_of_album_lyrics = [album.lyrics_processed for album in self.albums]
        artist_lyrics = " ".join(list_of_album_lyrics)
        return artist_lyrics

    @property
    def lyrics_analysed(self) -> dict:
        """Performs full analysis of all artist's lyrics."""
        return NLP.text_analyse(text=self.lyrics_processed)

    @classmethod
    def get_filename(cls, name: str) -> str:
        """Returns JSON file name of selected artist."""
        name = name.lower().replace(" ", "_")
        return f"{name}.json"

    @classmethod
    def load(cls, name: str) -> object:
        """Creates instance of this class, base on JSON file content."""
        # path to artist JSON file
        artist_file_path = os.path.join(config.DATA_DIR, cls.get_filename(name=name))
        # loads artist JSON file content
        json_content = FilesManager.load_json(path=artist_file_path)
        # if there is no artist data
        if not json_content:
            return None
        # dictionary that stores creation parameters
        parameters = {
            "name": json_content.get("name"),
            "image_url": json_content.get("image_url"),
            "albums": []
        }
        # iteration over albums in JSON file and collecting Albums objects
        for album in json_content["albums"]:
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
