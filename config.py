"""
Main configuration script.
"""


import os


# root application directory path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# templates directory path
TEMPLATES_DIR = os.path.join(BASE_DIR, "app/templates")

# static directory path
STATIC_DIR = os.path.join(BASE_DIR, "app/static")

# path to data storage directory
DATA_DIR = os.path.join(BASE_DIR, "data")

# logging configuraion
LOGGING = {
    "CONFIG_FILE": os.path.join(BASE_DIR, ".logs", "logging.conf")
}

# "on-demand" application mode switch
ON_DEMAND_MODE = False
