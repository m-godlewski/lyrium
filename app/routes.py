"""
Main backend routing script.
"""

from flask import render_template
from flask import request

from app import APP
from app import controller


@APP.route("/")
@APP.route("/index")
@APP.route("/home")
def index():
    """Renders landing page."""
    return render_template("home.html")


@APP.route("/analysis", methods=["POST"])
def analysis():
    """Renders specific artist lyrics analysis site."""

    # retrieving artist name from request
    artist_name = request.form["artist_name"]

    # calls method that makes artist lyrics analyse
    analysis_results = controller.lyrics_analyse_artist(name=artist_name)

    # ensures if artists exists in database
    if analysis_results.get("artist_exists", False):
        return render_template("analysis.html", data=analysis_results)
    else:
        return render_template("artist_not_found.html", data={"artist_name": artist_name})
