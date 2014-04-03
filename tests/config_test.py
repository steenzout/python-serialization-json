import company.package.config
import ConfigParser

import mock

import pytest

import unittest


from company.package.config import DEFAULT_CONFIG_FILE


class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        # mock of logging.RootLogger
        self.patch_get_logger = mock.patch('company.package.config.logging.getLogger')
        self.mock_get_logger = self.patch_get_logger.start()

        self.instance = self.mock_get_logger.return_value
        self.instance.debug.return_value = None
        self.instance.error.return_value = None
        self.instance.info.return_value = None

        self.addCleanup(self.patch_get_logger.stop)

    @mock.patch('company.package.config.os.path')
    @mock.patch('company.package.config.ConfigParser.read')
    def test_load_configuration(self, mock_read, mock_path):
        """
        Test company.config.load_configuration().
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = True
        mock_read.return_value = None

        company.package.config.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_read.assert_called_with(DEFAULT_CONFIG_FILE)

        self.assertTrue(self.mock_get_logger.called)
        self.instance.info.assert_called_once_with('%s configuration file was loaded.' % DEFAULT_CONFIG_FILE)

    @mock.patch('company.package.config.os.path')
    @mock.patch('company.package.config.ConfigParser.read')
    def test_load_configuration_nofile(self, mock_read, mock_path):
        """
        Test company.logging.load() when the configuration file doesn't exist.
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = False
        mock_read.return_value = None

        with pytest.raises(ValueError):
            company.package.config.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(mock_read.readConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.instance.error.assert_called_once_with('%s configuration file does not exist!' % DEFAULT_CONFIG_FILE)

    @mock.patch('company.package.config.os.path')
    @mock.patch('company.package.config.ConfigParser.read')
    def test_load_configuration_errors(self, mock_read, mock_path):
        """
        Test company.logging.load() when NoSectionErrors are raised.
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = True
        mock_read.side_effect = ConfigParser.NoSectionError("No section: 'formatters'")

        company.package.config.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(mock_read.readConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.instance.error.assert_called_once_with('Failed to load configuration from %s!' % DEFAULT_CONFIG_FILE)
        self.instance.debug.assert_called_once_with(
            str(ConfigParser.NoSectionError("No section: 'formatters'")), exc_info=True)
