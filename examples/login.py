#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import getpass

from babelcloud.account import Account

def main():
    account = Account.login(
            username = raw_input("username: "),
            password = getpass.getpass("password: "),
            provider = raw_input("provider: ")
            )
    print account

if __name__ == "__main__":
    main()

