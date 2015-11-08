"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
from flask import request, redirect, render_template
from functools import wraps

def auth(required_roles=None, sufficient_roles=None, redirect_url=None):
    """
    Specifies authorization rules to access a resource.
    :param required_roles: allows to specify all the required roles to access a resource
    :param sufficient_roles: allows to specify sufficient roles that grant access to a resource
    :param redirect_url: allows to specify the url to which redirect the user if the request is not an AJAX request

    Example:
    @auth() # requires simply the request principal to be authenticated
    @auth(required_roles=["admin", "user"], sufficient_roles=["superman"])
    """
    if sufficient_roles is None:
        sufficient_roles = []
    if required_roles is None:
        required_roles = []

    header_requested_with = "X-Requested-With"
    ajax_request_type = "XMLHttpRequest"

    def handle_unauthorized():
        if header_requested_with in request.headers and request.headers[header_requested_with] == ajax_request_type:
            # AJAX request;
            return "Unauthorized", 401

        if redirect_url is not None:
            return redirect(redirect_url)

        return render_template("error/401.html"), 401


    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not hasattr(request, "user"):
                # unauthorized
                return handle_unauthorized()

            principal = request.user
            if not principal.authenticated:
                return handle_unauthorized()

            for sufficient_role in sufficient_roles:
                if principal.is_in_role(sufficient_role):
                    return f(*args, **kwargs)

            for required_role in required_roles:
                if not principal.is_in_role(required_role):
                    return handle_unauthorized()

            # continue normally
            return f(*args, **kwargs)
        return wrapped
    return decorator


def requires_roles(*roles):
    """
    Specifies the required roles to access a resource.
    :param roles:
    :return:

    Example:
    @requires_roles() # requires simply the request principal to be authenticated
    @requires_roles("admin", "user")
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not hasattr(request, "user"):
                # unauthorized
                return render_template("error/401.html"), 401

            principal = request.user
            if not principal.authenticated:
                return render_template("error/401.html"), 401

            for required_role in roles:
                if not principal.is_in_role(required_role):
                    return render_template("error/401.html"), 401

            # continue normally
            return f(*args, **kwargs)
        return wrapped
    return decorator
