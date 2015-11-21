import json
from flask.ext.babel import gettext
from flask import Blueprint, request, render_template
from app.decorators.security.antiforgery import validate_aft
"""
    Defines the routes for the public area.
"""

public = Blueprint("public", __name__)

@public.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@public.route("/test", methods=["POST"])
@validate_aft()
def testaft():
    return "AFT validation succeeded", 200


