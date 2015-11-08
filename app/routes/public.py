import json
from flask.ext.babel import gettext
from flask import Blueprint, request, render_template
"""
    Defines the routes for the public area.
"""

public = Blueprint("public", __name__)

@public.route("/", methods=["GET"])
def index():
    return render_template("index.html")



