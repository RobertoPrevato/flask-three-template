import unittest

#
# import the test cases that need to be run
#
from tests.server_test import ServerTestCase
from tests.helpers_test import HelpersTestCase
from tests.membershipmongo_test import MembershipMongoTestCase
from tests.logmongo_test import LogMongoTestCase

if __name__ == '__main__':
    unittest.main(verbosity=2)