import company.package.logging

import ConfigParser

import mock

import pytest

import unittest


from company.package.logging import DEFAULT_CONFIG_FILE


class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        # mock of logging.RootLogger
        self.patch_get_logger = mock.patch('company.package.logging.logging.getLogger')
        self.mock_get_logger = self.patch_get_logger.start()

        self.mock_root_logger = self.mock_get_logger.return_value
        self.mock_root_logger.debug.return_value = None
        self.mock_root_logger.error.return_value = None
        self.mock_root_logger.info.return_value = None

        self.addCleanup(self.patch_get_logger.stop)

    @mock.patch('company.package.logging.os.path')
    @mock.patch('company.package.logging.logging.config.fileConfig')
    def test_load_configuration(self, mock_fileConfig, mock_path):
        """
        Test company.package.logging.load_configuration().
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = True
        mock_fileConfig.return_value = None

        company.package.logging.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_fileConfig.assert_called_with(DEFAULT_CONFIG_FILE, disable_existing_loggers=False)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.info.assert_called_once_with('%s configuration file was loaded.' % DEFAULT_CONFIG_FILE)

    @mock.patch('company.package.logging.os.path')
    @mock.patch('company.package.logging.logging.config.fileConfig')
    def test_load_configuration_nofile(self, mock_fileConfig, mock_path):
        """
        Test company.package.logging.load_configuration() when the configuration file doesn't exist.
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = False
        mock_fileConfig.return_value = None

        with pytest.raises(ValueError):
            company.package.logging.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(mock_fileConfig.fileConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with(
            '%s configuration file does not exist!' % DEFAULT_CONFIG_FILE)

    @mock.patch('company.package.logging.os.path')
    @mock.patch('company.package.logging.logging.config.fileConfig')
    def test_load_configuration_errors(self, mock_fileConfig, mock_path):
        """
        Test company.package.logging.load_configuration() when NoSectionErrors are raised.
        """
        mock_path.exists.return_value = True
        mock_path.isfile.return_value = True
        mock_fileConfig.side_effect = ConfigParser.NoSectionError("No section: 'formatters'")

        company.package.logging.load_configuration()

        mock_path.exists.assert_called_once_with(DEFAULT_CONFIG_FILE)
        mock_path.isfile.assert_called_once_with(DEFAULT_CONFIG_FILE)

        self.assertFalse(mock_fileConfig.fileConfig.called)

        self.assertTrue(self.mock_get_logger.called)
        self.mock_root_logger.error.assert_called_once_with(
            'Failed to load configuration from %s!' % DEFAULT_CONFIG_FILE)
        self.mock_root_logger.debug.assert_called_once_with(
            str(ConfigParser.NoSectionError("No section: 'formatters'")), exc_info=True)
