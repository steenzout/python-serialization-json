import sys
import os.path

import company.package.logging
import ConfigParser

import logging

import mock

import unittest


from company.package.logging import DEFAULT_LOGGING_CONFIG_FILE


class LoggingTestCase(unittest.TestCase):

    def test_load_configuration(self):
        """
        Test company.logging.load().
        """
        with mock.patch.object(os.path, 'exists', return_value=True) as mock_method1:
            with mock.patch.object(logging.config, 'fileConfig', return_value=None) as mock_method2:
                company.package.logging.load_configuration()

        mock_method1.assert_called_with(DEFAULT_LOGGING_CONFIG_FILE)
        mock_method2.assert_called_with(DEFAULT_LOGGING_CONFIG_FILE, disable_existing_loggers=False)

    def test_load_configuration_nofile(self):
        """
        Test company.logging.load() when the configuration file doesn't exist.
        """
        with mock.patch.object(os.path, 'exists', return_value=False) as mock_method1:
            with mock.patch.object(sys.stderr, 'write', return_value=None) as mock_method2:
                company.package.logging.load_configuration()

        mock_method1.assert_called_with(DEFAULT_LOGGING_CONFIG_FILE)
        mock_method2.assert_called_with(
            'Logging configuration file %s doesn\'t exist!\n' % DEFAULT_LOGGING_CONFIG_FILE)

    def test_load_configuration_errors(self):
        """
        Test company.logging.load() when NoSectionErrors are raised.
        """
        with mock.patch.object(os.path, 'exists', return_value=True) as mock_method1:
            with mock.patch.object(logging.config, 'fileConfig', return_value=None) as mock_method2:
                with mock.patch.object(sys.stderr, 'write', return_value=None) as mock_method3:
                    mock_method2.side_effect = ConfigParser.NoSectionError("No section: 'formatters'")
                    company.package.logging.load_configuration()

        mock_method1.assert_called_with(DEFAULT_LOGGING_CONFIG_FILE)
        mock_method2.assert_called_with(DEFAULT_LOGGING_CONFIG_FILE, disable_existing_loggers=False)
        mock_method3.assert_called()
