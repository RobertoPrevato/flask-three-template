"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Authentication strategy.
* Contains global request handler used for user authentication and session management.
"""
from core.encryption.aes import AesEncryptor
from flask import render_template, request
from bll.membership.membershipprovider import MembershipProvider
import sys


def authentication_handlers(app):
    """
     Registers a global request handler for authentication.

     NB: An alternative, if needed, is to initialize a membership provider for each logical area (e.g. admin, public, etc.);
     which allows to use different database structures to store accounts and sessions for different parts of
     the application and to have different, parallel authentication mechanisms.
     This template includes a global membership provider, because it is a simpler model that suffices in most cases.
    """

    if not hasattr(app, "membership"):
        raise Exception("The application is not initialized with a MembershipProvider.")

    membership_provider = app.membership

    # the name of the cookie used to store a session key
    session_cookie = "authtoken"
    SECURE_COOKIES = app.config["SECURE_COOKIES"]
    ENCRYPTION_KEY = app.config["ENCRYPTION_KEY"]


    def initialize_anonymous_session():
        client_ip = request.remote_addr
        result = membership_provider.initialize_anonymous_session(client_ip, {
            "user_agent": request.headers["User-Agent"] if "User-Agent" in request.headers else None
        })

        # set a flag to set a session cookie
        request.set_session_cookie = True
        principal = result["principal"]
        session = result["session"]

        # set information inside the request
        setattr(request, "user", principal)
        setattr(request, "session", session)


    @app.before_request
    def authenticate_request(*args, **kwargs):
        session_key = request.cookies.get(session_cookie)
        if session_key is None:
            # initialize an anonymous session
            initialize_anonymous_session()
        else:
            # decrypt
            session_guid = AesEncryptor.decrypt(session_key, ENCRYPTION_KEY)
            # try to perform login by session key
            success, result = membership_provider.try_login_by_session_key(session_guid)

            if success:
                # result is a principal object
                principal = result["principal"]
                session = result["session"]

                # set information inside the request
                setattr(request, "user", principal)
                setattr(request, "session", session)
            else:
                # initialize an anonymous session
                initialize_anonymous_session()


    @app.after_request
    def set_auth_cookie(response):
        set_session_cookie = hasattr(request, "set_session_cookie")
        unset_session_cookie = hasattr(request, "unset_session_cookie")
        if set_session_cookie:
            session = request.session
            session_guid = str(session.guid)
            # encrypt:
            session_token = AesEncryptor.encrypt(session_guid, ENCRYPTION_KEY)

            response.set_cookie(session_cookie,
                                value=session_token,
                                expires=session.expiration,
                                httponly=True,
                                secure=SECURE_COOKIES)
        if unset_session_cookie:
            # instruct the browser to delete the session cookie
            response.set_cookie(session_cookie, value="", expires=0)
        return response

