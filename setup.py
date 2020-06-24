#!/usr/bin/env python
#coding:utf8

from setuptools import find_packages,setup

setup(
        name = "bambo",
        version = '1.0.0',
        packages = find_pacakges(),
        include_package_data = True,
        zip_safe = False,
        install_requires = ['flask','click'],
        )

