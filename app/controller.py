"""
Script that contains methods responsible for business logic of application.
"""


import logging
import traceback

from app.classes import Artist


def lyrics_analyse_artist(name: str) -> dict:
    """Performs selected artist lyrics analysis."""
    try:

        # creates selected artist object
        artist = Artist.load(name=name)

        # checks if artist data was found
        if artist:
            # makes analysis of selected artist lyrics
            results = {
                "artist_exists": True,
                "artist_name": artist.name,
                "artist_image_url": artist.image_url,
                "analysis": artist.lyrics_analysed,
            }
        else:
            results = {
                "artist_exists": False,
                "artist_name": name,
                "artist_image_url": None,
                "analysis": None
            }

    except Exception:
        logging.error(traceback.format_exc())
        return {}
    else:
        return results
