"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
from flask import request, render_template
from functools import wraps

def ajax():
    """
    Specifies that the request must be performed using an AJAX request.
    """
    header_name = "X-Requested-With"
    ajax_request_type = "XMLHttpRequest"

    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if header_name not in request.headers or request.headers[header_name] != ajax_request_type:
                # return request not found; pretend that the server didn`t notice the request
                return render_template("error/404.html"), 404

            # continue normally
            return f(*args, **kwargs)
        return wrapped
    return decorator