# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.account. """

import unittest
import getpass

from babelcloud.account import Account

class AccountPropertiesTest(unittest.TestCase):
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

    def test_images_property(self):
        image = self.server.snapshot()
        self.assertIn(image, self.account.images)
        image.destroy()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AccountPropertiesTest))
    return suite

if __name__ == "__main__":
    unittest.main()

