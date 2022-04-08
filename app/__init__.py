import flask
import flask_restful
import flask_cors
import nltk
import logging
import logging.config
import yaml

import app
import config


# application logging configuration, based on logging.cfg file
logging.config.dictConfig(yaml.load(open(config.LOGGING["CONFIG_FILE"])))


# application and api main instances
APP = flask.Flask(__name__)
API = flask_restful.Api(APP)


# CORS configuration
flask_cors.CORS(APP)


# Downloading NLTK resources
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("universal_tagset")
nltk.download("averaged_perceptron_tagger")


from app import routes
from app import errors
