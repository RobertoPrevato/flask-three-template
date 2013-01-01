"""
* Copyright 2015, Roberto Prevato roberto.prevato@gmail.com
* https://github.com/RobertoPrevato/Flask-three-template
*
* Licensed under the MIT license:
* http://www.opensource.org/licenses/MIT
"""
import sys, traceback
from datetime import datetime
from core.collections.bunch import Bunch


class ReportsManager():
    """
    Provides business logic to log application specific messages in a database.
    """

    defaults =  {
      "store": None
    }


    def __init__(self, options = None):
        if options is None:
            options = {}
        params = dict(self.defaults, **options)
        self.validate_store_option(params)
        self.options = Bunch()
        self.options.merge(params)


    def get_messages(self, options):
        """
        Gets a paginated result of messages.
        :param options: pagination options
        :return: catalog page
        """
        if options is None:
            raise Exception("Missing pagination options.")
        options["search_properties"] = ["message"]
        return self.options.store.get_messages(options)


    def get_exceptions(self, options):
        """
        Gets a paginated result of exceptions.
        :param options: pagination options
        :return: catalog page
        """
        if options is None:
            raise Exception("Missing pagination options.")
        options["search_properties"] = ["type", "message", "callstack"]
        return self.options.store.get_exceptions(options)


    def log_message(self, message, kind = "Normal"):
        """
        Logs a message
        :param message: application message to store
        :param kind: kind of message
        """
        now = datetime.now()
        return self.options.store.store_message(message, now, kind)


    def log_exception(self, ex = None):
        """
        Logs an exception in database.
        :param ex: exception object
        """
        now = datetime.now()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if ex is None:
            ex = exc_value
        call_stack = "\n".join(traceback.format_tb(exc_traceback))
        message = ex.message if hasattr(ex, "message") \
            else exc_value.args[0] if len(exc_value.args) > 0 else str(ex)
        return self.options.store.store_exception(message, now, str(exc_type), call_stack)


    def try_log_exception(self, ex = None):
        """
        Tries to log an exception in database; does nothing if the log itself causes exception.
        :param ex: exception object
        """
        try:
            self.log_exception(ex)
        except Exception:
            pass


    def log_warning(self, message):
        """
        Logs a warning message
        :param message: application message to store
        """
        now = datetime.now()
        return self.options.store.store_message(message, now, "Warning")


    @staticmethod
    def validate_store_option(params):
        """
        Validates the store option passed when instantiating a ReportsManager.
        :param params: constructor options
        """
        if params["store"] is None:
          raise Exception("Missing `store` option")
        req = ["store_message",
               "store_exception",
               "get_messages",
               "get_exceptions"]
        for name in req:
            if not hasattr(params["store"], name):
                raise Exception("The given store does not implement `" + name + "` member")


