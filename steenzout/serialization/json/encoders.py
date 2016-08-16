# -*- coding: utf-8 -*-
#
# Copyright 2016 Pedro Salgado
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
.. module:: steenzout.serialization.json.encoders
    :synopsis: Company json.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

import calendar
import logging
import strict_rfc3339


LOGGER = logging.getLogger('steenzout.serialization.json.encoders')


def as_object(obj):
    """
    Return a JSON serializable type for ``o``.

    :param obj: the object to be serialized.
    :type obj: object

    :raises AttributeError: in case the given ``o`` is not a Python object.

    :return: JSON serializable type for the given object.
    """
    LOGGER.debug('as_object(%s)', obj)

    return obj.__dict__


def as_date(dat):
    """
    Return the RFC3339 UTC string representation of the given date and time.

    :param dat: the object/type to be serialized.
    :type dat: datetime.date

    :raises TypeError: in case the given ``o`` is not an instance of ``datetime.date``.

    :return: JSON serializable type for the given object.
    """
    LOGGER.debug('as_date(%s)', dat)

    return strict_rfc3339.timestamp_to_rfc3339_utcoffset(
        calendar.timegm(dat.timetuple()))
