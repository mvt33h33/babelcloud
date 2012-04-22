# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

class Image(object):
    def __init__(self, image = None):
        self._image = image

    @property
    def name(self):
        return self._image.name

    @property
    def provider(self):
        return self._image.provider

    @property
    def id(self):
        return self._image.id

