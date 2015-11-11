from flask import Blueprint, request, render_template
from flask.ext.babel import gettext
from app.decorators.security.auth import auth
from app import app
import json
"""
    Defines the routes for the administrative area.
"""

admin = Blueprint("admin", __name__)

@admin.route("/admin/login", methods=["GET"])
def adminlogin():
    """Renders the administrative side login page"""
    return render_template("admin/login.html", error=None)


@admin.route("/admin/auth", methods=["POST"])
def adminauth():
    """Responds to administrative side login post requests"""
    data = request.get_json()
    if data is None:
        return "Bad Request", 400, {"Content-Type": "text/plain"}

    email = data["email"]
    password = data["password"]
    remember = data["remember"]
    navigator = data["navigator"]

    if email == "" or password == "":
        return "Bad Request", 400, {"Content-Type": "text/plain"}

    client_ip = request.remote_addr
    success, result = app.membership.try_login(email, password, remember, {
        "navigator": navigator
    })

    if success:
        # result is a principal object
        principal = result["principal"]
        session = result["session"]

        # set information inside the request
        setattr(request, "user", principal)
        setattr(request, "session", session)

        # set a flag to set a session cookie
        request.set_session_cookie = True

        return json.dumps({
            "success": True
        })

    # NB: in some cases, for security reasons, don't disclose the exact reason why a Login fails
    # Imagine for example, if somebody would like to know whether an account with a certain email exist in a website.
    return json.dumps({
        "success": False
    })


@admin.route("/admin", methods=["GET"])
@auth(required_roles=["admin"], redirect_url="/admin/login")
def admindashboard():
    """Renders the administrative side dashboard"""
    return render_template("admin/index.html")
