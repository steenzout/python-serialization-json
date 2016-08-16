#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

exec(open('steenzout/serialization/json/version.py').read())

setup(
    name='steenzout.serialization.json',
    version=__version__,
    description='Steenzout JSON serialization package.',
    author='Pedro Salgado',
    author_email='steenzout@ymail.com',
    maintainer='Pedro Salgado',
    maintainer_email='steenzout@ymail.com',
    url='https://github.com/steenzout/python-serialization-json',
    namespace_packages=['steenzout', 'steenzout.serialization'],
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    install_requires=[
        str(pkg.req) for pkg in parse_requirements(
                'requirements.txt', session=pip.download.PipSession())],
    tests_require=[
        str(pkg.req) for pkg in parse_requirements(
                'test-requirements.txt', session=pip.download.PipSession())],
    license='Apache 2.0',
    classifiers=(
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy'
    )
)
