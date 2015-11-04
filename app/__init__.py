import logging
import logging.handlers
from flask import Flask
app = None


def setup_app(**config_overrides):
    """
      This is normal setup code for a Flask app, but we give the option
      to provide override configurations so that in testing, a different
      database can be used.
    """
    from app.global_handlers import global_handlers

    # we want to modify the global app, not a local copy
    global app

    app = Flask(__name__)

    # Load config then apply overrides
    app.config.from_object("app.config")
    app.config.update(config_overrides)

    # apply global configuration
    global_handlers(app)

    # register the application areas
    register_areas(app)

    # Register the logger
    register_logger(app)

    return app


def register_areas(app):
    # register the areas
    from app.routes.public import public
    from app.routes.admin import admin
    app.register_blueprint(public)
    app.register_blueprint(admin)


def register_logger(app):
    """Create an error logger and attach it to ``app``."""

    max_bytes = int(app.config["LOG_FILE_MAX_SIZE"]) * 1024 * 1024   # MB to B
    # Use "# noqa" to silence flake8 warnings for creating a variable that is
    # uppercase.  (Here, we make a class, so uppercase is correct.)
    Handler = logging.handlers.RotatingFileHandler  # noqa
    f_str = ('%(levelname)s @ %(asctime)s @ %(filename)s '
             '%(funcName)s %(lineno)d: %(message)s')

    access_handler = Handler(app.config["HTTP_LOG_NAME"],
                             maxBytes=max_bytes)
    access_handler.setLevel(logging.INFO)
    logging.getLogger("werkzeug").addHandler(access_handler)

    app_handler = Handler(app.config["APP_LOG_NAME"], maxBytes=max_bytes)
    formatter = logging.Formatter(f_str)
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)
    app.logger.addHandler(app_handler)

