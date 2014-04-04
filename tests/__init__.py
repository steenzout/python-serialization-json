"""
.. module:: company.package.tests
    :platform: Unix
    :synopsis:

.. moduleauthor:: Your Name <email address>
"""

import os

import company.package.config
import company.package.logging

import logging

import unittest


LOGGING_CONFIG_FILE = '%s/tests/logging.conf' % os.curdir
PACKAGE_CONFIG_FILE = '%s/tests/package.cfg' % os.curdir


class Basic(object):
    """
    Basic functionality to enhance test cases.
    """

    __slots__ = ('configuration', 'logger')

    configuration_loaded = False
    logging_loaded = False

    def setup_configuration(self):
        """
        Setup test configuration.
        It will also load (once) the test configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_configuration()')

        if not Basic.configuration_loaded:
            company.package.config.reset()
            company.package.config.load_configuration(PACKAGE_CONFIG_FILE)
            Basic.configuration_loaded = True

        self.configuration = company.package.config.get()

    def setup_logger(self):
        """
        Setup test logger.
        It will also load (once) the test logging configuration.
        """
        logging.getLogger('%s.%s' % (__name__, 'Basic')).info('setup_logger()')

        if not Basic.logging_loaded:
            company.package.logging.load_configuration(LOGGING_CONFIG_FILE)
            Basic.logging_loaded = True

        self.logger = logging.getLogger('%s.%s' % (__name__, self.__class__.__name__))


class BaseTestCase(unittest.TestCase, Basic):
    """
    Base test case.
    """

    def setUp(self):
        """
        Setup test resources:
        1. load logging configuration
        2. load package configuration
        """
        # 1
        self.setup_logger()
        self.logger.info('setUp()')

        # 2
        self.setup_configuration()

    def tearDown(self):
        """
        Tears down test resources:
        1. remove temporary test database
        """
        self.logger.info('tearDown()')
