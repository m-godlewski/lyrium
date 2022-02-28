"""
Main backend routing script.
"""

from flask import jsonify
from flask import render_template
from flask import request

from app import APP
from app import controller


# @APP.route("/")
@APP.route("/index")
@APP.route("/home")
def index():
    """
    """
    return render_template("home.html")


@APP.route("/")
@APP.route("/analyse", methods=["GET"])
def analyse():
    """
    """
    # retrieving artist name from request
    # artist_name = request.args.get("artist_name")
    # TODO temporary static name set to test purposes
    artist_name = "Gojira"

    # calls method that makes artist lyrics analyse
    results_of_analyse = controller.lyrics_analyse_artist(artist_name=artist_name)

    # returns endpoint response
    # return jsonify(
    #     {
    #         "artist_name": artist_name,
    #         "results": results_of_analyse
    #     }
    # ), 200

    return render_template("home.html", artist_name=artist_name, analysis=results_of_analyse)
