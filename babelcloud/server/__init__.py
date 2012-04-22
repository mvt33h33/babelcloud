# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

class Server(object):
    def __init__(self, node = None, driver = None):
        self._node = node
        self._driver = driver

    @property
    def name(self):
        return self._node.name

    @property
    def state(self):
        return self._node.state

    @property
    def ips(self):
        return self._node.public_ips

    @property
    def provider(self):
        return self._node.provider

    def destroy(self):
        self._driver.destroy_node()

