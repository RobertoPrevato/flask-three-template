from flask import Blueprint, render_template

"""
    Defines the routes for the administrative area.
"""

admin = Blueprint("admin", __name__)


@admin.route("/", methods=["GET"])
def index():
    return render_template("index.html")



