# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

import time

from libcloud.compute.types import NodeState

class Server(object):
    def __init__(self, node = None):
        """Initializes a logical interface for dealing with a cloud server.

        {
            'extra': {
                'flavorId': '2', 
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

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __ne__(self, other):
        return not self == other

    @property
    def name(self):
        return self._node.name

    @property
    def state(self):
        while True:
            nodes = [ node for node in self._node.driver.list_nodes() if Server(node) == self ]
            if len(nodes):
                self._node = nodes[0]
                break
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
        return self._node.extra["hostId"]

    @property
    def uri(self):
        return self._node.extra["uri"]

    @property
    def provider(self):
        return self._node.provider

    def destroy(self):
        self._node.destroy()

    def wait(self):
        while self.state != "running":
            time.sleep(1)

    def snapshot(self):
        raise NotImplementedError()

    def reboot(self):
        self._node.reboot()

