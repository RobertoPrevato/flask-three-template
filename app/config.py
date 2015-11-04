from os import path, pardir

# Flask configurations
HOST = "0.0.0.0"
PORT = 44660
DEBUG = False # NB: if the debugger is active, is not possible to debug using PyCharm

# Keys
ENCRYPTION_KEY = "LOREM_IPSUM"

# Main database configuration: data access layer project
DAL_PROJECT = "dalmongo"

# Whether to set the "Secure" cookie option (HTTPS only, or not)
SECURE_COOKIES = False

# Application supported cultures (e.g. en-us; or simply en):
DEFAULT_CULTURE = "en"
CULTURES = {
  "en": "English"
}

# Meta copy: of course, change this with your copyright
COPYRIGHT = "Copyright 2015 Roberto Prevato roberto.prevato@gmail.com"

# Base directory
BASEDIR = path.abspath(path.join(path.dirname(__file__), pardir))

# Logging configurations
LOG_FILE_MAX_SIZE = "256" # in MB
APP_LOG_NAME = "logs/app.log"
HTTP_LOG_NAME = "logs/http.log"
