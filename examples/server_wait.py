#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import getpass
import time

from babelcloud.account import Account

def main():
    account = Account.login(
            username = raw_input("username: "),
            password = getpass.getpass("password: "),
            provider = raw_input("provider: ")
            )
    server = account.create_server(
            name = "example_babelcloud",
            image = account.images[0],
            size = account.sizes[0]
            )

    print server.state
    while server.state != "running":
        time.sleep(3)
        print server.state

if __name__ == "__main__":
    main()

