"""
.. module:: package.config
    :platform: Unix
    :synopsis: Configuration utilities.

.. moduleauthor:: Your Name <email address>
"""

from __future__ import absolute_import

import os.path

try:
    from ConfigParser import SafeConfigParser as ConfigParser
except ImportError:
    from configparser import ConfigParser

import logging


DEFAULT_CONFIG_FILE = '/etc/package/package.cfg'

settings = None


def load_configuration(config_file=DEFAULT_CONFIG_FILE):
    """
    Loads configuration.

    :param config_file: the configuration file(s).
    :type config_file: str or list of str
    """
    global settings

    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        msg = '%s configuration file does not exist!' % config_file
        logging.getLogger(__name__).error(msg)
        raise ValueError(msg)

    parser = ConfigParser()
    try:
        parser.read(config_file)
        settings = {}
        for section in parser.sections():
            settings[section] = dict(parser.items(section))
        logging.getLogger(__name__).info('%s configuration file was loaded.' % config_file)
        return settings
    except StandardError as error:
        settings = None
        msg = 'Failed to load configuration from %s!' % config_file
        logging.getLogger(__name__).error(msg)
        logging.getLogger(__name__).debug(str(error), exc_info=True)
        raise error


def get():
    """
    Returns the configuration.

    :return: the configuration.
    :rtype: object (configParser.ConfigParser)
    """
    if settings is None:
        return load_configuration()
    return settings


def reset():
    """
    Reset the configuration.
    """
    global settings

    settings = None
