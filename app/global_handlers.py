from flask import url_for
from flask.ext.babel import Babel
from app.errors_handlers import errors_handlers

def global_handlers(app):
    """
        Registers application global handlers.
    """
    from app.helpers.resources import Resources

    supported_cultures = app.config["CULTURES"]

    # TODO: enable only for development
    @app.route('/<path:path>')
    def static_proxy(path):
        return app.send_static_file(path)

    # localization:
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        # TODO: implement here the logic to get the culture by request.
        #return request.accept_languages.best_match(supported_cultures.keys())
        return "en"

    # register error handlers
    errors_handlers(app)

    # template helpers
    @app.context_processor
    def add_helpers():
        """
        Adds a dictionary of helper variables and functions into Jinja templates.
        It is sufficient to add the values into the helpers dictionary, thanks to @app.context_processor decorator.
        """
        copy = app.config["COPYRIGHT"]
        def get_copy():
            return copy
        helpers = {
            "static": lambda filename: url_for("static", filename=filename),
            "resources": Resources,
            "copy": get_copy
        }
        return helpers

    @app.after_request
    def add_header(response):
        """
        Add headers.
        """
        response.headers["Cache-Control"] = "public, max-age=0"
        return response
