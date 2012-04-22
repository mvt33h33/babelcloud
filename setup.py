#!/usr/bin/env python -t3
# -*- coding: utf-8 -*-

# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

from distutils.core import setup

setup_params = {}
setup_params['name'] = "babelcloud"
setup_params['version'] = "0.1"
setup_params['description'] = ''.join([
    "Python library for translatin libcloud into models.",
    ])
setup_params['long_description'] = ''.join([
    "The python module allows a more pythonic access to cloud providers and ",
    "utilizes the libcloud library underneath but provides a simpler API to ",
    "make programming against cloud environments even easier.",
    ])
setup_params['author'] = "Alex Brandt"
setup_params['author_email'] = "alex.brandt@rackspace.com"
setup_params['url'] = "https://github.com/alunduil/babelcloud"
setup_params['license'] = ""
setup_params['packages'] = [
        "babelcloud",
        ]
setup_params['data_files'] = [
        ("share/doc/%s-%s" % (setup_params['name'], setup_params['version']), [
            "README",
            "examples/login.py"
            ]),
        ]
setup_params['requires'] = [
        ]

setup(**setup_params)

