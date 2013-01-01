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


@admin.route("/admin/logout", methods=["GET"])
@auth(required_roles=["admin"], redirect_url="/admin/login")
def adminlogout():
    """Logs out the current user"""
    # destroy the session
    principal = request.user
    app.membership.destroy_session(principal.session.guid)

    # set a flag to set a session cookie
    request.unset_session_cookie = True
    return render_template("admin/logout.html")


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


@admin.route("/admin/getusers", methods=["POST"])
@auth(required_roles=["admin"])
def admingetusers():
    """Returns the list of application users"""
    data = request.get_json()
    if data is None:
        return "Missing filters data.", 400, {"Content-Type": "text/plain"}

    data = app.membership.get_accounts(data)
    return json.dumps(data.__dict__)


@admin.route("/admin/getmessages", methods=["POST"])
@auth(required_roles=["admin"])
def admingetmessages():
    """Returns the list of application messages"""
    data = request.get_json()
    if data is None:
        return "Missing filters data.", 400, {"Content-Type": "text/plain"}

    data = app.reports.get_messages(data)
    # formatting is responsibility of presentation layer
    for o in data.subset:
        o["timestamp"] = o["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps(data.__dict__)


@admin.route("/admin/getexceptions", methods=["POST"])
@auth(required_roles=["admin"])
def admingetexceptions():
    """Returns the list of application exceptions"""
    data = request.get_json()
    if data is None:
        return "Missing filters data.", 400, {"Content-Type": "text/plain"}

    data = app.reports.get_exceptions(data)
    # formatting is responsibility of presentation layer
    for o in data.subset:
        o["timestamp"] = o["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps(data.__dict__)