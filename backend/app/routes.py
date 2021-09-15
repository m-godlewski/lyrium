"""
Main backend routing script.
"""

from flask import jsonify
from flask import request

from app import APP
from app import controller


@APP.route("/analyse", methods=["GET"])
def analyse():
    """
    """
    # retrieving artist name from request
    artist_name = request.args.get("artist_name")

    # calls method that makes artist lyrics analyse
    results_of_analyse = controller.lyrics_analyse_artist(artist_name = artist_name)

    return jsonify(
        {
            "artist_name": artist_name,
            "results": results_of_analyse
        }
    ), 200
