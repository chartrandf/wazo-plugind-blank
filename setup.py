#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from setuptools import find_packages
from setuptools import setup

setup(
    name='wazo_plugind_blank',
    version='0.1',

    description='Blank plugin to test install',

    author='Francis Chartrand',
    author_email='fchartrand@wazo.io',

    url='https://wazo.io',

    entry_points={
        'wazo_dird.views': [
            'wazo_plugind_blank = src.driver:MyDriver',
        ]
    }
)