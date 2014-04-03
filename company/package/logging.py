"""
.. module:: company.package.logging
    :platform: Unix
    :synopsis: Logging utilities.

.. moduleauthor:: Your Name <email address>
"""

from __future__ import absolute_import


import sys
import os

import ConfigParser

import logging.config


DEFAULT_CONFIG_FILE = '/etc/package/logging.conf'


def load_configuration(config_file=DEFAULT_CONFIG_FILE):
    """
    Loads logging configuration from the given configuration file.

    :param config_file: the configuration file (default=/etc/package/logging.conf)
    :type config_file: str
    """
    if not os.path.exists(config_file) or not os.path.isfile(config_file):
        msg = '%s configuration file does not exist!' % config_file
        logging.getLogger(__name__).error(msg)
        raise ValueError(msg)

    try:
        logging.config.fileConfig(config_file, disable_existing_loggers=False)
    except ConfigParser.NoSectionError as e:
        msg = 'Failed to load configuration from %s!' % config_file
        logging.getLogger(__name__).error(msg)
        logging.getLogger(__name__).debug(str(e), exc_info=True)
