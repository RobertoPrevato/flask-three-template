from flask import Blueprint, render_template
"""
    Defines the routes for the administrative area.
"""

admin = Blueprint("admin", __name__)

@admin.route("/admin/login", methods=["GET"])
def adminlogin():
    return render_template("admin/login.html")
