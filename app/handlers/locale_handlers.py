"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Localization strategy.
*
"""
from flask import url_for, request
from flask.ext.babel import Babel

def locale_handlers(app):
    """
        Registers application handlers for the localization strategy.
    """
    def get_request_locale():
        default_culture = app.config["DEFAULT_CULTURE"]
        cultures = app.config["CULTURES"].keys()

        # if the culture is set in the header, then use it (needed to ensure consistency when multiple tabs are open)
        header_value = request.headers.get("X-Request-Culture")
        if header_value and header_value in cultures:
            # set and exit
            return header_value

        # if the user identity is known, support user favorite language
        user = request.user if hasattr(request, "user") else None
        if user is not None and user.culture:
            user_culture = user.culture
            if user_culture and user_culture in cultures:
                return user_culture

        culture_cookie = request.cookies.get("culture")
        if culture_cookie and culture_cookie in cultures:
            return culture_cookie

        # set culture by browser setting, or application default
        best_match = request.accept_languages.best_match(cultures)
        if best_match:
            return best_match

        return default_culture


    # localization:
    babel = Babel(app)
    @babel.localeselector
    def get_locale():
        locale = get_request_locale()
        request.culture = locale
        return locale


    @app.after_request
    def add_culture_cookie(response):
        culture = request.culture if hasattr(request, "culture") else None
        if culture:
            response.set_cookie("culture", value=culture)
        return response

