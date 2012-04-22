# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.account.login. """

import unittest
import getpass

from babelcloud.account import Account, LoginError

class LoginTest(unittest.TestCase):
    """Testing suite for babelcloud.account.login."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_successful_account_login(self):
        self.assertIsNotNone(Account.login(
            username = raw_input("\nusername: "),
            password = getpass.getpass("password: "),
            provider = raw_input("provider: ")
            ))

    def test_unsuccessful_account_login(self):
        self.assertRaises(LoginError, Account.login,
                username = "incorrect_user_name_never_used_anywhere_i_hope",
                password = "incorrect_user_name_never_used_anywhere_i_hope",
                provider = "rackspace",
                )

