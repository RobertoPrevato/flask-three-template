import server
import unittest


class ServerTestCase(unittest.TestCase):
    """
      Generic server tests.
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


    def test_homepage(self):
        rv = self.app.get('/')
        assert "<title>" in rv.data
