# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

"""Primary testing suite for babelcloud.server."""

import unittest
import getpass

from test_babelcloud import ACCOUNT

from babelcloud.account import Account

class ServerExistenceTest(unittest.TestCase):
    """Testing suite for babelcloud.server and server existence."""

    def test_create_and_destroy_server(self):
        server = ACCOUNT.create_server(
                name = "test_babelcloud.test_server",
                image = self.account.images[0],
                size = self.account.sizes[0]
                )
        server.wait()
        self.assertTrue(server in ACCOUNT.servers, "Server not created!")
        server.destroy()
        self.assertTrue(server not in ACCOUNT.servers, "Server not destroyed!")

class ServerManipulationTest(unittest.TestCase):
    """Testing suite for babelcloud.server and server manipulation."""

    def setUp(self):
        self.server = ACCOUNT.create_server(
                name = "test_babelcloud.test_server",
                image = self.account.images[0],
                size = self.account.sizes[0]
                )

    def tearDown(self):
        self.server.wait()
        self.server.destroy()

    def test_snapshot_server(self):
        self.server.wait()
        image = self.server.snapshot()
        self.assertIn(image, ACCOUNT.images)

    def test_suspend_server(self):
        self.server.wait()
        self.server.suspend()
        self.assertEqual("suspended", self.server.status)

    def test_wait_for_server(self):
        self.assertNotEqual("running", self.server.status)
        self.server.wait()
        self.assertEqual("running", self.server.status)
        pass

    def test_reboot_server(self):
        self.server.wait()
        self.server.reboot()

    def test_reset_root_password(self):
        self.server.wait()
        self.server.reset_root_password("just_testing")
        # TODO Login to the server and check the password ...

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ServerExistenceTest))
    suite.addTest(unittest.makeSuite(ServerManipulationTest))
    return suite

if __name__ == "__main__":
    unittest.main()

