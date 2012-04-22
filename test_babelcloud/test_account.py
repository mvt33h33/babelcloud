# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.account. """

import unittest
import getpass

from babelcloud.account import Account

class AccountTest(unittest.TestCase):
    """Testing suite for babelcloud.account."""

    @classmethod
    def setUpClass(cls):
        while True:
            cls.account = Account.login(
                    username = raw_input("\nusername: "),
                    password = getpass.getpass("password: "),
                    provider = raw_input("provider: ")
                    )
            if cls.account:
                break

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.server = self.account.create_server(
                name = "test_babelcloud",
                image = self.account.images[0],
                size = self.account.sizes[0]
                )
        self.server.wait()

    def tearDown(self):
        self.server.destroy()

    def test_servers_property(self):
        """Check that servers contains the server we create."""
        self.assertIn(server, self.account.servers)

