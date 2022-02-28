"""
Main configuration script.
"""


import os


# root application directory path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# path to data storage directory
DATA_DIR = os.path.join(BASE_DIR, "data")

# logging configuraion
LOGGING = {
    "CONFIG_FILE": os.path.join(BASE_DIR, ".logs", "logging.conf")
}
