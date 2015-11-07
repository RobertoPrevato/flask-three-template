"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Represents a generic MembershipProvider utilized to manage Membership for an application.
* It can be used to handle global authentication; or per-area authentication.
* Contains business logic for Login, Logout, ChangePassword.
"""
from bll.membership.membershipprovider import MembershipProvider

def register_membership(app):
    """
     Initialize an application global membership provider.
     NB:
     an alternative, if needed, is to initialize a membership provider for each logical area (e.g. admin, public, etc.);
     which allows to use different database structures to store accounts and sessions for different parts of
     the application and to have different, parallel authentication mechanisms.
     This template includes a global membership provider, because it is a simpler model that suffices in most cases.
    """
    DAL_PROJECT = app.config["DAL_PROJECT"]
    # initialize an application membership provider
    # NB: an alternative, if needed, is to initialize a membership provider for each area (e.g. admin and public areas)
    membership_store = None
    if DAL_PROJECT == "dalmongo":
        from dalmongo.membership.membershipstore import MembershipStore
        membership_store = MembershipStore()
    else:
        raise Exception("MembershipStore for `{}` implemented".format(DAL_PROJECT))

    # instantiate the membership provider
    provider = MembershipProvider({ "store": membership_store })

    # attach to the application
    setattr(app, "membership", provider)


