import json
from flask import Blueprint, request, render_template
from app.decorators.crossdomain import crossdomain
from core.encryption.aes import AesEncryptor
from bll.managers.users.profiles_manager import ProfilesManager
"""
    Defines the routes for the public area.
"""

public = Blueprint("public", __name__)
from flask.ext.babel import gettext

@public.route("/", methods=["GET"])
def index():
    return render_template("index.html")



