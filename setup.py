#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('steenzout/serialization/json/version.py').read())

setup(name='steenzout.serialization.json',
      version=__version__,
      description='Steenzout JSON serialization json.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/python-serialization-json',
      namespace_packages=('steenzout', 'steenzout.serialization',),
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[
            str(pkg.req) for pkg in parse_requirements(
                    'requirements.txt', session=pip.download.PipSession())],
      tests_require=[
            str(pkg.req) for pkg in parse_requirements(
                    'test-requirements.txt', session=pip.download.PipSession())],)
