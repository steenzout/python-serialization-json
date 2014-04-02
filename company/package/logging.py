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


DEFAULT_LOGGING_CONFIG_FILE = '/etc/package/logging.conf'


def load_configuration(config_file=DEFAULT_LOGGING_CONFIG_FILE):
    """
    Loads logging configuration from the given configuration file.

    :param config_file: the configuration file (default=/etc/noesis/logging.conf)
    :type config_file: str
    """
    if os.path.exists(config_file):
        try:
            logging.config.fileConfig(config_file, disable_existing_loggers=False)
        except ConfigParser.NoSectionError as e:
            sys.stderr.write('Fail: %s\n' % e)
    else:
        sys.stderr.write('Logging configuration file %s doesn\'t exist!\n' % config_file)
