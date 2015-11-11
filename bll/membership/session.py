"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""

class Session:
    """
    Generic object used for session management.
    """
    def __init__(self, obj_id, guid, userkey, expiration, anonymous):
        self.id = obj_id
        self.guid = guid
        self.userkey = userkey
        self.expiration = expiration
        self.anonymous = anonymous


    @staticmethod
    def from_dict(data):
        """
        Returns an instance of Session, from a dictionary.
        :param data: session data in dictionary.
        :return: Session
        """
        return Session(data["id"],
                       data["guid"],
                       data["userkey"] if "userkey" in data else None,
                       data["expiration"],
                       data["anonymous"])
