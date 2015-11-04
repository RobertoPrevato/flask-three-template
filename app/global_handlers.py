from flask import render_template, request, url_for
from flask.ext.babel import Babel, gettext
import sys


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


    @app.errorhandler(Exception)
    def exception_handler(error):
        """Handle uncaught exceptions."""
        app.logger.error("Uncaught Exception", exc_info=sys.exc_info())
        app.handle_exception(error)

    @app.errorhandler(400)
    def bad_request(error):
        """Handle 400 errors."""
        return render_template("error/400.html"), 400

    @app.errorhandler(401)
    def not_authorized(error):
        """Handle 401 errors."""
        return render_template("error/401.html"), 401

    @app.errorhandler(403)
    def forbidden(error):
        """Handle 403 errors."""
        return render_template("error/403.html"), 403

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return render_template("error/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        """Handle 405 errors."""
        return render_template("error/405.html", method=request.method), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        """Handle 500 errors."""
        return render_template("error/500.html"), 500

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
