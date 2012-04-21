# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import re

from libcloud.compute.types import Provider, InvalidCredsError
from libcloud.compute.providers import get_driver

class Account(object):
    @classmethod
    def login(cls, username, password, provider = ""):
        drivers = [ 
                get_driver(Provider.__dict__[name]) for name in Provider.__dict__ \
                        if type(Provider.__dict__[name]) == int \
                        and re.search(provider, name, re.I) 
                ]

        print "drivers: ",drivers

        fail = False

        for driver in drivers:
            try:
                fail = False
                cls._connection = driver(username, password)

                print "connection: ",cls._connection
                
                cls.servers = [ 
                        Server(node) for node in cls._connection.list_nodes()
                        ]

                print "servers: ", cls.servers
            except InvalidCredsError:
                fail = True
                continue

        print "fail: ",fail

        if fail:
            raise LoginError([ 
                name for name in Provider.__dict__ \
                        if Provider.__dict__[name] in drivers
                ])

        return cls

class LoginError(RuntimeError):
    pass

