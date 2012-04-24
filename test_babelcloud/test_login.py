# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.account.login. """

import unittest
import getpass

from test_babelcloud import ACCOUNT
from babelcloud.account import Account, LoginError

class LoginTest(unittest.TestCase):
    """Testing suite for babelcloud.account.login."""

    def test_successful_account_login(self):
        self.assertIsNotNone(ACCOUNT)

    def test_unsuccessful_account_login(self):
        self.assertRaises(LoginError, Account.login,
                username = "incorrect_user_name_never_used_anywhere_i_hope",
                password = "incorrect_user_name_never_used_anywhere_i_hope",
                provider = "rackspace",
                )

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTest))
    return suite

if __name__ == "__main__":
    unittest.main()

