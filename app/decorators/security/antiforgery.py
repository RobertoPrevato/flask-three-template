"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import re
import uuid
from core.encryption.aes import AesEncryptor
from flask import request, render_template
from functools import wraps
from app.config import SECURE_COOKIES

header_name = "X-AFT"
form_name = "aft"
cookie_name = "aftck"
header_requested_with = "X-Requested-With"
ajax_request_type = "XMLHttpRequest"


def validate_aft(redirect_url=None):
    """
    Specifies that the request should perform antiforgery token validation AJAX request.
    Utilizes dual token strategy (session based encrypted token, issued in both cookie and page);
    sent at each request in both cookie and request header, for ajax requests or form values;
    """

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
            if re.match("^(get|options|head)$", request.method, re.IGNORECASE):
                return f(*args, **kwargs)

            # check if the session is defined inside the request
            if not request.session:
                raise Error("missing session inside the request object; use the AntiforgeryValidate after the membership provider")
            encryption_key = request.session.guid

            # get the tokens: one is always in the cookie; the second may be inside form or request header
            # request header is more important, assuming that pages implement AJAX requests, rather than form submission
            cookie_token = request.cookies.get(cookie_name)
            second_token = request.headers[header_name] if header_name in request.headers else None

            if second_token is None:
                # try to read from form
                second_token = request.form[form_name] if form_name in request.form else None

            # are the tokens present?
            if not cookie_token or not second_token:
                return handle_unauthorized()

            # decrypt the tokens; decryption will fail if the tokens were issued for another session;
            a, cookie_token = AesEncryptor.try_decrypt(cookie_token, encryption_key)
            b, second_token = AesEncryptor.try_decrypt(second_token, encryption_key)

            if not a or not b or not cookie_token or not second_token:
                return handle_unauthorized()

            # are the tokens identical?
            if cookie_token != second_token:
                return handle_unauthorized()

            # validation succeeded
            # continue normally
            return f(*args, **kwargs)
        return wrapped
    return decorator


def issue_aft_token():
    """
    Issues a new antiforgery token to include in a page request.
    If it doesn't exist in the request, sets a cookie in the response.
    @param request
    @returns {string} the newly defined
    """
    # check if the session is defined inside the request
    if not request.session:
        raise Error("missing session inside the request object; use the AntiforgeryValidate after the membership provider")
    encryption_key = request.session.guid

    cookie_token = request.cookies.get(cookie_name)
    new_token_defined = False
    if not cookie_token:
        #define a new token
        cookie_token = uuid.uuid1()
        new_token_defined = True
    else:
        can_decrypt, value = AesEncryptor.try_decrypt(cookie_token, encryption_key)
        if not can_decrypt:
            cookie_token = uuid.uuid1()
            new_token_defined = True
        else:
            # use the same value of before
            cookie_token = value

    if new_token_defined:
        cookie_token = str(cookie_token)
        encrypted_token = AesEncryptor.encrypt(cookie_token, str(encryption_key))
        # the cookie will be set in response object inside global_handlers function
        request.set_aft_cookie = encrypted_token

    # return the token encrypted with AES; many calls always return a different value
    return AesEncryptor.encrypt(cookie_token, encryption_key)
