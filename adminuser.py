"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Utility script to administer the application users.
"""
import argparse

separator = "******************************************************\n"

parser = argparse.ArgumentParser(description= "Adds users to the application, using the configured DAL project.",
                                 epilog = "{}\n{}".format("author: Roberto Prevato roberto.prevato@gmail.com", separator))

parser.add_argument("-k", "--userkey", dest= "userkey",
                    required=True, help="User key, when performing login (e.g. email address)")

parser.add_argument("-p", "--password", dest= "password",
                    required=False, help="User password")

parser.add_argument("-o", "--operation", dest="operation",
                    required=True, choices=["add", "delete", "setroles"],
                    help="Operation to perform: add user, delete user, set roles")

parser.add_argument("-r", "--roles", nargs='+', dest= "roles",
                    required=False, help="User roles")

args = parser.parse_args()

from app.config import DAL_PROJECT
from bll.membership import MembershipProvider

# initialize an application membership provider
membership_store = None
if DAL_PROJECT == "dalmongo":
    from dalmongo.membership.membershipstore import MembershipStore
    membership_store = MembershipStore()
else:
    raise Exception("MembershipStore for `{}` not implemented".format(DAL_PROJECT))

# instantiate the membership provider
membership = MembershipProvider({ "store": membership_store })

def main(options):
    if not options.operation:
        options.operation = "add"

    success = False
    result = ""

    if options.operation == "add":
        # password is required
        if not options.password:
            print("error: argument -p/--password is required")
            return

        success, result = membership.create_account(options.userkey, options.password, None, options.roles)
        if success:
            print("Account created successfully")

    elif options.operation == "delete":
        success, result = membership.delete_account(operations.userkey)
        if success:
            print("Account deleted successfully")

    elif options.operation == "setroles":
        # roles are required
        if not options.roles:
            print("error: argument -r/--roles is required")
            return

        success, result = membership.update_account(options.userkey, {
            "roles": options.roles
        })
        if success:
            print("Account updated successfully")

    if not success:
        print("ERROR: " + result)

main(args)
