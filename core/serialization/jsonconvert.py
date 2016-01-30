"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import json


def datetime_handler(obj):
    return obj.strftime("%Y-%m-%d %H:%M:%S") if hasattr(obj, "strftime") else obj


def shortdate_handler(obj):
    return obj.strftime("%Y-%m-%d") if hasattr(obj, "strftime") else obj


def isodate_handler(obj):
    return obj.isoformat() if hasattr(obj, "isoformat") else obj


class Json:


    @staticmethod
    def serialize(data, handler=None):
        if data is None:
            return json.dumps(None)

        if hasattr(data, "to_json"):
            return data.to_json()

        if handler is None:
            handler = isodate_handler

        if hasattr(data, "__dict__"):
            return Json.serialize(data.__dict__, handler)

        return json.dumps(data, default=handler)
