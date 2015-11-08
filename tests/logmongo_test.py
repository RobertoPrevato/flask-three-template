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
* Tests for the log in MongoDB.
"""
import server
import unittest
from bll.reports.reportsmanager import ReportsManager

from dalmongo import db
from dalmongo.reports.reportsstore import ReportsStore


class LogMongoTestCase(unittest.TestCase):
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

    def test_log(self):
        """
        Tests the log functions.
        """
        store = ReportsStore()
        log = ReportsManager({ "store": store })
        pagination = {
            "page": 1,
            "size": 500,
            "search": None
        }

        messages_before = log.get_messages(pagination)

        data = log.log_message("Log Test")

        messages_after = log.get_messages(pagination)

        assert len(messages_after.subset) == (len(messages_before.subset) + 1)

        exceptions_before = log.get_exceptions(pagination)

        try:
            a = 10 // 0
        except Exception as ex:
            ex = log.log_exception(ex)

        exceptions = log.get_exceptions(pagination)
        assert len(exceptions.subset) == (len(exceptions_before.subset) + 1)

