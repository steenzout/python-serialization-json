"""
.. module:: company.package.config
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


class Cache(object):
    SETTINGS = None


def load_configuration(config_file=DEFAULT_CONFIG_FILE):
    """
    Loads configuration.

    :param config_file: the configuration file(s).
    :type config_file: str or list of str
    """
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        msg = '%s configuration file does not exist!' % config_file
        logging.getLogger(__name__).error(msg)
        raise ValueError(msg)

    parser = ConfigParser()
    try:
        parser.read(config_file)
        Cache.SETTINGS = {}
        for section in parser.sections():
            Cache.SETTINGS[section] = dict(parser.items(section))
        logging.getLogger(__name__).info('%s configuration file was loaded.', config_file)
        return Cache.SETTINGS
    except StandardError as error:
        SETTINGS = None
        logging.getLogger(__name__).error('Failed to load configuration from %s!', config_file)
        logging.getLogger(__name__).debug(str(error), exc_info=True)
        raise error


def get():
    """
    Returns the configuration.

    :return: the configuration.
    :rtype: object (configParser.ConfigParser)
    """
    if Cache.SETTINGS is None:
        return load_configuration()
    return Cache.SETTINGS


def reset():
    """
    Reset the configuration.
    """
    Cache.SETTINGS = None
