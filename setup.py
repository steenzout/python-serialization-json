#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

execfile('company/package/version.py')

setup(name='primogen',
      version=__version__,
      description='Python basic package.',
      author='Pedro Salgado',
      author_email='steenzout@ymail.com',
      maintainer='Pedro Salgado',
      maintainer_email='steenzout@ymail.com',
      url='https://github.com/steenzout/python-primogen',
      namespace_packages=('company',),
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests', 'company')),
      install_requires=[
            str(pkg.req) for pkg in parse_requirements(
                    'requirements.txt', session=pip.download.PipSession())],
      tests_require=[
            str(pkg.req) for pkg in parse_requirements(
                    'test-requirements.txt', session=pip.download.PipSession())],)
