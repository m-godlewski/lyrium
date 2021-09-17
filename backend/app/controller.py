"""
Script that contains methods responsible for business logic of application.
"""

import logging
import traceback

from app.classes import Track, Album, Artist


def lyrics_analyse_artist(artist_name: str) -> dict:
    """
    """
    try:

        # dictionary that stores analyse results
        results = {}

        # creates selected artist object
        artist = Artist.load(name=artist_name)

        # makes analysis of selected artist lyrics
        results = artist.make_analysis()

    except Exception:
        logging.error(traceback.format_exc())
        return {}
    else:
        return results
