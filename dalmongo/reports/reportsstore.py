"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import uuid
from dalmongo import db
from dalmongo.mongostore import MongoStore
from core.collections.bunch import Bunch

class ReportsStore(MongoStore):
    """
    Represents a storage manager for MongoDB based application reports.
    """

    defaults =  {
      "messages_collection": "app_messages",
      "exceptions_collection": "app_exceptions"
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

        messages_collection = opt.messages_collection
        exceptions_collection = opt.exceptions_collection

        if messages_collection not in db_collections:
            # create the messages collection
            messages = db.create_collection(messages_collection)

        if exceptions_collection not in db_collections:
            # create the sessions collection
            exceptions = db.create_collection(exceptions_collection)

        return self


    def store_message(self, message, time, kind = "Normal"):
        """
        Stores an application message in database.
        :param message: message to store
        :param time: timestamp
        :param kind: the kind of message (e.g. Normal, Warning, etc.)
        :return: message data
        """
        collection = db[self.options.messages_collection]
        data = {
          "message": message,
          "timestamp": time,
          "kind": kind
        }

        result = collection.insert_one(data)
        message_id = result.inserted_id
        data = collection.find_one({ "_id": message_id })
        return self.normalize_id(data)


    def store_exception(self, message, time, typename, callstack):
        """
        Stores an application exception in database.
        :param ex: exception to store
        :param time: timestamp
        :param callstack: exception callstack
        :return: data stored in db
        """
        collection = db[self.options.exceptions_collection]
        data = {
          "message": message,
          "timestamp": time,
          "type": typename,
          "callstack": callstack
        }

        result = collection.insert_one(data)
        ex_id = result.inserted_id
        data = collection.find_one({ "_id": ex_id })
        return self.normalize_id(data)


    def get_messages(self, options):
        """
        Gets a paginated subset of application messages.
        """
        collection = db[self.options.messages_collection]
        data = self.get_catalog_page(collection, options)
        return data


    def get_exceptions(self, options):
        """
        Gets a paginated subset of application exceptions.
        """
        collection = db[self.options.exceptions_collection]
        data = self.get_catalog_page(collection, options)
        return data
