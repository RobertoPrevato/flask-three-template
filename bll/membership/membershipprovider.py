"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
*
* Generic MembershipProvider utilized to manage Membership for an application.
* It can be used to handle global authentication; or per-area authentication.
* Contains business logic for Login, Logout, ChangePassword.
"""
import random
import hashlib
import re
import datetime
from core.collections.bunch import Bunch
from bll.membership.principal import Principal
from bll.membership.session import Session


class MembershipProvider:
    """
        Provides business logic to provide user authentication.
    """

    defaults =  {
      "store": None,
      "short_time_expiration": 1e3 * 60 * 20,
      "long_time_expiration": 1e3 * 60 * 60 * 24 * 365,
      "failed_login_attempts_limit": 4,
      "minutes_limit": 15,
      "requires_account_confirmation": False
    }


    def __init__(self, options = None):
        if options is None:
            options = {}
        params = dict(self.defaults, **options)
        self.validate_store_option(params)
        self.options = Bunch()
        self.options.merge(params)


    @staticmethod
    def get_hash(password, salt):
        """
        Returns an hashed version of password, created using the given salt
        :param salt: salt to use to hash a password
        :return: hashed version of password
        """
        key = (password + salt).encode("utf-8")
        return hashlib.sha224(key).hexdigest()


    @staticmethod
    def get_new_salt():
        """
        Returns a new salt to be used to hash password
        :return: {String} new salt to be used to hash passwords
        """
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(ALPHABET) for i in range(16))


    @staticmethod
    def validate_store_option(params):
        """
        Validates the store option passed when instantiating a MembershipProvider.
        :param params: constructor options
        """
        if params["store"] is None:
          raise Exception("Missing `store` option")
        req = ["get_account",
               "get_session",
               "create_account",
               "update_account",
               "create_session",
               "destroy_session",
               "save_session_data",
               "get_session_data",
               "get_failed_login_attempts",
               "save_login_attempt"]
        for name in req:
            if not hasattr(params["store"], name):
                raise Exception("The given store does not implement `" + name + "` member")


    def get_account(self, userkey):
        """
        Gets the account with the given key.
        :param userkey: key of the user (e.g. email or username)
        """
        data = self.options.store.get_account(userkey)
        if data is None:
            return None
        result = Bunch()
        result.merge(data)
        return result


    def create_account(self, userkey, password, data = None):
        """
        Creates a new user account in db
        :param userkey: key of the user (e.g. email or username)
        :param password: account clear password (e.g. user defined password)
        :param data: dict, optional account data
        :return:
        """
        # verify that an account with the same key doesn't exist already
        account_data = self.options.store.get_account(userkey)
        if account_data is not None:
            return False, "AccountAlreadyExisting"
        if data is None:
            data = {}
        salt = self.get_new_salt()
        hashedpassword = self.get_hash(password, salt)
        now = datetime.datetime.now()

        if self.options.requires_account_confirmation:
            # set a confirmation token inside the account data
            data["confirmation_token"] = uuid.uuid1()
        return True, self.options.store.create_account(userkey, hashedpassword, salt, data)


    def delete_account(self, userkey):
        """
        Deletes the account with the given userkey
        :param userkey: the user key (email address or username)
        :return: success, error
        """
        account = self.options.store.get_account(userkey)
        if account is None:
            return False, "AccountNotFound"
        self.options.store.delete_account(userkey)
        return True


    def confirm_account(self, userkey):
        """
        Confirms the account with the given userkey.
        :param userkey: the user key (email address or username)
        :return: success, error
        """
        return self.update_account(userkey, {
            "confirmed": True
        })


    def ban_account(self, userkey):
        """
        Bans the account with the given userkey.
        :param userkey: the user key (email address or username)
        :return: success, error
        """
        return self.update_account(userkey, {
            "banned": True
        })


    def update_account(self, userkey, data):
        """
        Updates the account with the given key; setting the data.
        :param userkey: the user key (email address or username)
        :param data: account data to update
        :return: self
        """
        account = self.options.store.get_account(userkey)
        if account is None:
            return False, "AccountNotFound"
        self.options.store.update_account(userkey, data)
        return True, None


    def try_login(self, userkey, password, remember, client_ip, client_data = None, options = None):
        """
        Tries to perform a login for the user with the given key (e.g. email or username); password;
        :param userkey: the user key (email address or username)
        :param password:
        :param remember: whether to have a longer expiration time or not
        :param client_ip: ip of the client for which the function has been called
        :param client_data: optional client data
        :param options: extra options
        :return:
        """
        # get account data
        account_data = self.get_account(userkey)
        if account_data is None:
            return False, "AccountNotFound"

        login_attempts = self.get_failed_login_attempts(userkey)
        tooManyAttempts = self.options.failed_login_attempts_limit <= login_attempts
        if tooManyAttempts:
            return False, "TooManyAttempts"
            # error: too many attempts in the last minutes, for this user

        check_password = options is None or options["automatic_no_password"] is None

        if check_password:
            # generate hash of given password, appending salt
            hsh = self.get_hash(password, account_data.salt)
            if account_data.hash != hsh:
                # the key exists, but the password is wrong
                self.report_login_attempt(userkey, client_ip)
                # exit
                return False, "WrongPassword"

        # check if the account is confirmed
        if self.options.requires_account_confirmation and not account_data.confirmed:
            return False, "RequireConfirmation"

        # check if the account was banned
        if hasattr(account_data, "banned") and account_data.banned == True:
            return False, "BannedAccount"

        # get session expiration
        expiration = self.get_new_expiration(remember)
        # save session
        session = self.options.store.create_session(userkey, expiration, client_ip, client_data)

        return True, {
            "principal": Principal(account_data.id,
                                   account_data,
                                   session,
                                   True),
            "session": Session.from_dict(session)
        }

    def report_login_attempt(self, userkey, client_ip):
        """
        Reports a login attempt.
        :param userkey: the user key (email address or username)
        :param client_ip: ip of the client
        """
        now = datetime.datetime.now()
        self.options.store.save_login_attempt(userkey, client_ip, now)
        return self


    def change_password(self, userkey, password_reset_key, new_password):
        pass


    def get_failed_login_attempts(self, userkey):
        """
        Gets the number of failed login attempts for a userkey in the amount of minutes defined by MinutesLimit option.
        :param userkey: the user key (email address or username)
        """
        now = datetime.datetime.now()
        ms = self.options.minutes_limit * 60 * 1e3
        start = now - datetime.timedelta(milliseconds=ms)
        count = self.options.store.get_failed_login_attempts(userkey, start, now)
        return count


    def try_login_by_session_key(self, sessionkey):
        """
        Tries to perform login by user session key.
        :param sessionkey:
        :return: boolean, session, account
        """
        # returns bool, principal
        if sessionkey is None:
            return False, None

        session = self.options.store.get_session(sessionkey)
        if session is None:
            return False, None

        # convert into a class
        session = Session.from_dict(session)

        now = datetime.datetime.now()
        if session.expiration < now:
            return False, None

        if session.anonymous:
            return True, {
            "principal": Principal(None,
                                   None,
                                   session,
                                   False),
            "session": session
        }

        # get account data
        account = self.options.store.get_account(session.user_id)
        # return session and account data
        return True, {
            "principal": Principal(account_data["id"],
                                   account_data,
                                   session,
                                   True),
            "session": session
        }


    def initialize_anonymous_session(self, client_ip, client_data):
        """
        Initializes a session for an anonymous user.
        :param client_ip:
        :param navigator:
        :return:
        """
        expiration = self.get_new_expiration()
        userkey = False
        # save session
        session = self.options.store.create_session(userkey, expiration, client_ip, client_data)
        return {
            "principal": Principal(None, None, session, False),
            "session": Session.from_dict(session)
        }


    def get_new_expiration(self, remember = None):
        """
        Returns the expiration for a new session, based on the provider settings and if the user wants to be remembered.
        for longer or not.
        :param remember: boolean
        :return: datetime
        """
        if remember is None:
            remember = False
        now = datetime.datetime.now()
        ms = self.options.long_time_expiration if remember else self.options.short_time_expiration
        expiration = now + datetime.timedelta(milliseconds=ms)
        return expiration


    def save_session_data(self, sessionkey, data):
        """
        Stores session data in the database.
        :param sessionkey: the key of the session
        :param data: dictionary of data to store in database
        :return:
        """
        self.options.store.save_session_data(sessionkey, data)
        return self


    def get_session_data(self, sessionkey):
        """
        Gets the data associated with the given session, in database.
        :param sessionkey: the key of the session
        :return: dict
        """
        return self.options.get_session_data(sessionkey)


    def destroy_session(self, sessionkey):
        """
        Destroys the session with the given key.
        :param sessionkey: key of the session to destroy.
        :return: self
        """
        self.options.store.destroy_session(sessionkey)
        return self


    @staticmethod
    def validate_password(password_one, password_two):
        """
        Validates the two given passwords.
        :param password_one: first password written by user.
        :param password_two: password confirmation.
        :return: success, error
        """
        if not password_one or not password_two:
            return False, "missing password"
        if password_one != password_two:
            return False, "password mismatch"
        v = password_two
        rx = {
          "enforce": "^(?=.*\d)(?=.*[a-zA-Z\.\,\;\@\$\!\?\#\*\-\_\%\&]).{9,}$"
        }
        if not re.match(rx["enforce"], v):
            return False, "password too weak"
        return True, None