"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""

class Principal:
    """
        Generic security principal used to implement authentication.
    """
    def __init__(self, _id, identity, session, authenticated):
        self.id = _id
        self.identity = identity
        self.culture = None # TODO: favorite culture
        self.session = session
        self.authenticated = authenticated


    def is_in_role(self, role):
        """
        Returns true if the principal identity has a role, false otherwise.
        :param role: string role name.
        :return: bool
        """
        if self.identity is None:
            return False
        return role in self.identity.roles
