# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.server."""

import unittest
import getpass

from babelcloud.account import Account

class ServerExistenceTest(unittest.TestCase):
    """Testing suite for babelcloud.server and server existence."""

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

    def test_create_and_destroy_server(self):
        """Check if we can properly create servers."""
        server = self.account.create_server()
        self.assertTrue(server in self.account.servers, "Server not created!")
        server.destroy()
        self.assertTrue(server not in self.account.servers, "Server not destroyed!")

class ServerManipulationTest(unittest.TestCase):
    """Testing suite for babelcloud.server and server manipulation."""

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

        print cls.account

    def setUp(self):
        self.server = self.account.create_server(
                name = "babelcloud",
                image = self.account.images[0],
                size = self.account.sizes[0]
                )

    def tearDown(self):
        self.server.destroy()

    def test_snapshot_server(self):
        pass

    def test_suspend_server(self):
        pass

    def test_wait_for_server(self):
        pass

    def test_reboot_server(self):
        pass

    def test_reset_root_password(self):
        pass

