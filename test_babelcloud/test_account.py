# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.account. """

import unittest
import getpass

from test_babelcloud import ACCOUNT

from babelcloud.account import Account

class AccountPropertiesTest(unittest.TestCase):
    """Testing suite for babelcloud.account."""

    def setUp(self):
        self.server = ACCOUNT.create_server(
                name = "test_babelcloud.test_account",
                image = self.account.images[0],
                size = self.account.sizes[0]
                )
        self.server.wait()

    def tearDown(self):
        self.server.destroy()

    def test_servers_property(self):
        self.assertIn(self.server, ACCOUNT.servers)

    @unittest.skip("snapshot not supported in libcloud")
    def test_images_property(self):
        image = self.server.snapshot()
        self.assertIn(image, ACCOUNT.images)
        image.destroy()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AccountPropertiesTest))
    return suite

if __name__ == "__main__":
    unittest.main()

