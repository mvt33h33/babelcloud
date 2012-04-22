# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import re

from libcloud.compute.types import Provider, InvalidCredsError, LibcloudError
from libcloud.compute.providers import get_driver

from babelcloud.server import Server
from babelcloud.server.image import Image
from babelcloud.decorators import servererrorhandler

class Account(object):
    def __init__(self, connection):
        self._connection = connection

    @property
    @servererrorhandler
    def servers(self):
        return [ Server(node) for node in self._connection.list_nodes() ]

    @property
    @servererrorhandler
    def images(self):
        return [ Image(image) for image in self._connection.list_images() ]

    @property
    @servererrorhandler
    def sizes(self):
        return self._connection.list_sizes()

    @staticmethod
    def login(username, password, provider = ""):
        drivers = [ 
                get_driver(Provider.__dict__[name]) for name in Provider.__dict__ \
                        if type(Provider.__dict__[name]) == int \
                        and re.search(provider, name, re.I) 
                ]

        fail = False
        error = None

        for driver in drivers:
            try:
                fail = False
                account = Account(driver(username, password))
                account.servers
            except (InvalidCredsError, LibcloudError) as error:
                fail = True
                continue
            break

        if fail:
            raise LoginError(error, [ 
                name for name in Provider.__dict__ \
                        if Provider.__dict__[name] in drivers
                ])

        return account

    @servererrorhandler
    def create_server(self, name, image, size, **kargs):
        return Server(self._connection.create_node(name = name, image = image, size = size, **kargs))

class LoginError(RuntimeError):
    pass

