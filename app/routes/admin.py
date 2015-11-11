from flask import Blueprint, request, render_template
from flask.ext.babel import gettext
from app.decorators.security.auth import auth
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
    data = request.form
    username = data["username"]
    password = data["password"]

    if username == "" or password == "":
        return render_template("admin/login.html", error=gettext("error.InvalidFormData"))

    # TODO; this is left as todo intentionally;
    return "TODO"


@admin.route("/admin", methods=["GET"])
@auth(required_roles=["admin"], redirect_url="/admin/login")
def admindashboard():
    """Renders the administrative side dashboard"""
    return render_template("admin/index.html")
