from flask import url_for, request
from app.handlers.errors_handlers import errors_handlers
from app.handlers.locale_handlers import locale_handlers

def global_handlers(app):
    """
        Registers application global handlers.
    """
    from app.helpers.resources import Resources

    if app.config["DEVELOPMENT"]:
        # the server is running for development, so use it also to serve static files
        @app.route('/<path:path>')
        def static_proxy(path):
            return app.send_static_file(path)

    # register locale handlers
    locale_handlers(app)

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
    def add_headers(response):
        """
        Add headers.
        """
        response.headers["Cache-Control"] = "public, max-age=0"
        return response
