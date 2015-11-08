"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import uuid
from pymongo import ASCENDING
from dalmongo import db
from dalmongo.mongostore import MongoStore
from core.collections.bunch import Bunch

class MembershipStore(MongoStore):
    """
    Represents a Sessions and Accounts Storage manager for MongoDB utilized to manage Membership for an application.
    It can be used to handle global authentication; or per-area authentication.
    Contains data access logic for accounts and sessions.
    """

    defaults =  {
      "accounts_collection": "accounts",
      "sessions_collection": "sessions",
      "login_attempts_collection": "login_attempts",
      "user_key_field": "email"
    }


    def __init__(self, options = None):
        if options is None:
            options = {}
        params = dict(self.defaults, **options)
        self.options = Bunch()
        self.options.merge(params)
        self.configure()


    def configure(self):
        """
        Configure the db, creating the needed collections and theirs indexes.
        :return: self
        """
        opt = self.options
        db_collections = db.collection_names(include_system_collections=False)

        accounts_collection = opt.accounts_collection
        sessions_collection = opt.sessions_collection
        login_attempts_collection = opt.login_attempts_collection
        user_key_field = opt.user_key_field

        if accounts_collection not in db_collections:
            # create the account collection
            accounts = db.create_collection(accounts_collection)
            accounts.create_index([(user_key_field, ASCENDING)])

        if sessions_collection not in db_collections:
            # create the sessions collection
            sessions = db.create_collection(sessions_collection)
            sessions.create_index([(user_key_field, ASCENDING)])
            sessions.create_index([("guid", ASCENDING)])

        if login_attempts_collection and login_attempts_collection not in db_collections:
            # create the login attempts collection
            login_attempts = db.create_collection(login_attempts_collection)
            login_attempts.create_index([(user_key_field, ASCENDING)])

        return self


    def get_account_condition(self, userkey):
        """
        Returns account search condition.
        :param userkey: user key
        :return: condition for a mongodb search
        """
        a = {
            self.options.user_key_field: userkey
        }
        return a


    def get_account(self, userkey):
        """
        Gets the account data associated with the user with the given key.
        :param userkey: user key
        :return:
        """
        collection = db[self.options.accounts_collection]
        condition = self.get_account_condition(userkey)
        data = collection.find_one(condition)
        return self.normalize_id(data)


    def get_session(self, sessionkey):
        """
        Gets the session with the given key.
        :param sessionkey: session guid
        :return:
        """
        collection = db[self.options.sessions_collection]
        data = collection.find_one({ "guid": sessionkey })
        return self.normalize_id(data)


    def create_session(self, userkey, expiration, client_ip, client_data):
        """
        Creates a session in the database.
        :param userkey: key of the user for whom we are initializing the session
        :param expiration: expiration datetime of the session
        :param client_ip: ip of the client for whom this function is invoked
        :param client_data: client speficif information (e.g. browser navigator)
        :return:
        """
        collection = db[self.options.sessions_collection]
        data = {
          "guid": str(uuid.uuid1()),
          self.options.user_key_field: userkey,
          "anonymous": userkey == False,
          "expiration": expiration,
          "client_ip": client_ip,
          "client_data": client_data
        }

        result = collection.insert_one(data)
        session_id = result.inserted_id
        data = collection.find_one({ "_id": session_id })
        return self.normalize_id(data)


    def create_account(self, userkey, hashedpassword, salt, data):
        """
        Creates a new account
        :param userkey: user key (e.g. email or username)
        :param hashedpassword: hashed password
        :param salt: salt used to hash the account password
        :param data: extra account data
        """
        collection = db[self.options.accounts_collection]
        account_data = {
            self.options.user_key_field: userkey,
            "hash": hashedpassword,
            "salt": salt,
            "data": data
        }
        result = collection.insert_one(account_data)
        return {
            "id": str(result.inserted_id)
        }


    def save_session_data(self, sessionkey, data):
        """
        Stores data for the session with the given key.
        :param sessionkey: session guid.
        :param data: session data
        """
        collection = db[self.options.sessions_collection]
        condition = {
            "guid": sessionkey
        }
        update = {
            "data": data
        }
        collection.update_one(condition, update)


    def get_session_data(self, sessionkey):
        """
        Gets the data associated with the session with the given key.
        :param sessionkey: session guid.
        """
        collection = db[self.options.sessions_collection]
        condition = {
            "guid": sessionkey
        }
        session = collection.find_one(condition)
        return session["data"]


    def destroy_session(self, sessionkey):
        collection = db[self.options.sessions_collection]
        condition = {
            "guid": sessionkey
        }
        collection.delete_one(condition)


    def get_failed_login_attempts(self, userkey, start, end):
        """
        Gets the number of failed login attempts for a user with a given key, in the last minutes.
        :param userkey: key of the user for whom we are initializing the session
        :param start: start datetime to check for login attempts
        :param end: end datetime to check for login attempts
        :return:
        """
        condition = {
            self.options.user_key_field: userkey,
            "created": { "$gte": start, "$lt": end }
        }
        collection = db[self.options.login_attempts_collection]
        attempts = collection.find(condition)
        return attempts.count()


    def save_login_attempt(self, userkey, client_ip, time):
        """
        Stores a failed login attempt in database
        :param userkey: key of the user for whom the login attempt must be stored
        :param client_ip: ip of the client for which the method is invoked
        :param time: timestamp of the login attempt
        :return:
        """
        data = {
            self.options.user_key_field: userkey,
            "client_ip": client_ip,
            "created": time
        }
        collection = db[self.options.login_attempts_collection]
        collection.insert_one()


    def update_account(self, userkey, data):
        """
        Updates the account associated to the user with the given key.
        :param userkey: key of the user whose account must be deleted
        :param data: new account data
        """
        collection = db[self.options.accounts_collection]
        self.get_account_condition(userkey)
        collection.update_one(condition, data)


    def delete_account(self, userkey):
        """
        Deletes the account associated to the user with the given key.
        :param userkey: key of the user whose account must be deleted
        """
        collection = db[self.options.accounts_collection]
        condition = self.get_account_condition(userkey)
        collection.delete_one(condition)
