# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import time

from libcloud.compute.types import NodeState

class Server(object):
    def __init__(self, node = None):
        """Initializes a logical interface for dealing with a cloud server.

        {
            'extra': {
                'flavorId': '2', 
                'uri': 'https://servers.api.rackspacecloud.com/v1.0/644854/servers/20647550', 
                'hostId': '810723d694a4bf6e3419a608a89eef3e', 
                'password': None, 
                'metadata': {}
            }, 
            'image': None, 
            '_uuid': None, 
            'state': 0, 
            'size': None, 
            'id': '20647550'
        }

        """

        self._node = node

    @property
    def name(self):
        return self._node.name

    @property
    def state(self):
        self._node = [ node for node in self._node.driver.list_nodes() if node.uuid == self._node.uuid ][0]
        return [ name.lower() for name in NodeState.__dict__ if NodeState.__dict__[name] == self._node.state ][0]

    @property
    def ips(self):
        return list(set(self.public_ips) + set(self.private_ips))

    @property
    def public_ips(self):
        return self._node.public_ips

    @property
    def private_ips(self):
        return self._node.private_ips

    @property
    def image(self):
        return Image(self._node.extra["imageId"])

    @property
    def uuid(self):
        return self._node.uuid

    @property
    def provider(self):
        return self._node.provider

    def destroy(self):
        self._node.driver.destroy()

    def wait(self):
        while self.state != "running":
            time.sleep(1)

