#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('steenzout/serialization/json/metadata.py').read())

setup(
    name='steenzout.serialization.json',
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url=__url__,
    namespace_packages=['steenzout'],
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    package_data={'': ['LICENSE', 'NOTICE.md']},
    install_requires=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements.txt', session=pip.download.PipSession())],
    tests_require=[
        str(pkg.req) for pkg in parse_requirements(
            'requirements-test.txt', session=pip.download.PipSession())],
    license=__license__,
    classifiers=__classifiers__)
