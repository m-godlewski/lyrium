"""
Main configuration script.
"""


import os


# ROOT APPLICATION DIRECTORY PATH
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# LOGGING CONFIGURAION
LOGGING = {
    "CONFIG_FILE": os.path.join(BASE_DIR, ".logs", "logging.conf")
}
