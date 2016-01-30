from flask import Blueprint, request, render_template
from flask.ext.babel import gettext
from app.decorators.security.auth import auth
from app.decorators.security.antiforgery import validate_aft
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
@validate_aft()
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
    success, result = app.membership.try_login(email, password, remember, client_ip, {
        "user_agent": request.headers["User-Agent"] if "User-Agent" in request.headers else None,
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
    for o in data.subset:
        o["timestamp"] = o["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps(data.__dict__)


@admin.route("/admin/saveuser", methods=["POST"])
@auth(required_roles=["admin"])
def adminsaveuser():
    """Returns the list of application users"""
    data = request.get_json()
    if data is None:
        return "Missing data.", 400, {"Content-Type": "text/plain"}

    """
    TODO: idempotent method.
    if data["id"]:
        # edit account
        success, result = app.membership.update_account(data)
    else:
        # create account
        success, result = app.membership.create_account(data)

    return json.dumps(data.__dict__)
    """
    return "Not implemented", 500, {"Content-Type": "text/plain"}


@admin.route("/admin/getuserdetails", methods=["POST"])
@auth(required_roles=["admin"])
def admingetuserdetails():
    data = request.form
    if not data or "id" not in data:
        return "Missing id.", 400, {"Content-Type": "text/plain"}

    data = app.membership.get_account_by_id(data["id"])
    if data is None:
        return json.dumps(None)
    return json.dumps(data.__dict__)


@admin.route("/admin/getuserformdata", methods=["POST"])
@auth(required_roles=["admin"])
def admingetuserformdata():
    """
    Returns the data required to render the user form (e.g. the list of application supported roles)
    It should also contain the object data structure.
    """
    data = {
        "roles": [
            "admin",
            "superuser",
            "customer",
            "sgherro",
            "beholder"
        ] # application supported roles
    }
    return json.dumps(data)


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


@admin.route("/admin/getsessions", methods=["POST"])
@auth(required_roles=["admin"])
def admingetsessions():
    """Returns the list of current users sessions"""
    data = request.get_json()
    if data is None:
        return "Missing filters data.", 400, {"Content-Type": "text/plain"}

    data = app.membership.get_sessions(data)
    # formatting is responsibility of presentation layer
    for o in data.subset:
        o["expiration"] = o["expiration"].strftime("%Y-%m-%d %H:%M:%S")
        o["timestamp"] = o["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps(data.__dict__)