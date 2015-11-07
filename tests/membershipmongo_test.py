"""
* Flask-three-template 1.0.0
* https://github.com/RobertoPrevato/Flask-three-template
*
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* http://ugrose.com
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Tests for the membership feature.
"""
import server
import unittest
from bll.membership.membershipprovider import MembershipProvider

from dalmongo import db
from dalmongo.membership.membershipstore import MembershipStore


class MembershipMongoTestCase(unittest.TestCase):
    """
      Membership tests.
    """
    def setUp(self):
        """
          The code in the setUp() method is called before each individual test function is run.
        """
        self.app = server.app.test_client()


    def tearDown(self):
        """
          The code in the setUp() method is called before each individual test function is run.
        """
        pass


    def test_store_configuration(self):
        """
        Tests that the Mongo MembershipStore properly creates the collections in the database.
        """
        store = MembershipStore()

        db_collections = db.collection_names(include_system_collections=False)

        assert store.options.accounts_collection in db_collections
        assert store.options.sessions_collection in db_collections
        if store.options.login_attempts_collection:
            assert store.options.login_attempts_collection in db_collections

    def test_membership_create_session(self):
        """
        Tests the membership create session functions.
        """
        store = MembershipStore()
        provider = MembershipProvider({ "store": store })

        success, error = provider.try_login("foo@foo.it", "1568.Kop$2", False, "no-ip")
        assert success == False and error == "AccountNotFound"

        # create account
        userkey = "roberto.prevato@foo.com"
        password = "1568.Kop$2"

        # delete the account (may be there due to previous failed test)
        provider.delete_account(userkey)

        success, result = provider.create_account(userkey, password)

        # the first time, it should work
        assert success == True

        # get account data
        account = store.get_account(userkey)
        assert account is not None

        # try to create again the same account, this time it shouldn't work
        success, result = provider.create_account(userkey, "1568.Kop$2")
        assert success == False and result == "AccountAlreadyExisting"

        # try to create a session for this account
        login_success, data = provider.try_login(userkey, password, False, "no-ip")

        assert login_success == True
        principal = data["principal"]
        session = data["session"]

        # now delete the account
        provider.delete_account(userkey)

        account = provider.get_account(userkey)
        assert account is None


    def test_membership_validatepassword(self):
        """
        Tests the password validation logic.
        """
        store = MembershipStore()
        provider = MembershipProvider({ "store": store })

        password_one = "1568.Kop$2"
        password_two = "1568.asdas"

        valid, error = provider.validate_password(password_one, password_two)
        assert valid == False

        password_one = "easy" # too easy
        password_two = "easy"
        valid, error = provider.validate_password(password_one, password_two)
        assert valid == False and error == "password too weak"

        password_one = "1568.Kop$2"
        password_two = "1568.Kop$2"

        valid, error = provider.validate_password(password_one, password_two)
        assert valid == True