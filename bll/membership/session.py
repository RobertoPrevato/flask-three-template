"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Generic object used for session management.
"""

class Session:

    def __init__(self, obj_id, guid, user_id, expiration, anonymous):
        self.id = obj_id
        self.guid = guid
        self.user_id = user_id
        self.expiration = expiration
        self.anonymous = anonymous


    @staticmethod
    def from_dict(data):
        return Session(data["id"],
                       data["guid"],
                       data["user_id"] if "user_id" in data else None,
                       data["expiration"],
                       data["anonymous"])
