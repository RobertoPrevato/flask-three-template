import server
import unittest


class HelpersTestCase(unittest.TestCase):
    """
      Custom template helpers tests.
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


    def test_resources_helper(self):
        from app.helpers.resources import resources, load_resources_config
        # verify that no exception happen while reading the current resources configuration
        load_resources_config()

        test_conf = {
            "bundling": False,
            "minification": False,
            "sets": {
                "libs": [
                    "/scripts/jquery.js",
                    "/scripts/knockout.js",
                    "/scripts/lodash.js"
                ]
            }
        }

        a = resources("libs", test_conf)
        assert a == '<script src="/scripts/jquery.js"></script>\n<script src="/scripts/knockout.js"></script>\n<script src="/scripts/lodash.js"></script>'

        test_conf["bundling"] = True
        a = resources("libs", test_conf)
        assert a == '<script src="/scripts/libs.built.js"></script>'

        test_conf["minification"] = True
        a = resources("libs", test_conf)
        assert a == '<script src="/scripts/libs.min.js"></script>'

        assert True == True
