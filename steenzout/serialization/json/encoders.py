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
"""JSON encoders module."""

import calendar
import datetime
import inspect
import logging
import strict_rfc3339


LOGGER = logging.getLogger('steenzout.serialization.json.encoders')


def as_object(obj):
    """Return a JSON serializable type for ``o``.

    Args:
        obj (:py:class:`object`): the object to be serialized.

    Raises:
        :py:class:`AttributeError`:
            when ``o`` is not a Python object.

    Returns:
        (dict): JSON serializable type for the given object.
    """
    LOGGER.debug('as_object(%s)', obj)

    if isinstance(obj, datetime.date):
        return as_date(obj)

    elif hasattr(obj, '__dict__'):

        # populate dict with visible attributes
        out = {k: obj.__dict__[k] for k in obj.__dict__ if not k.startswith('_')}

        # populate dict with property names and values
        for k, v in (
                (p, getattr(obj, p))
                for p, _ in inspect.getmembers(
                    obj.__class__,
                    lambda x: isinstance(x, property))
        ):
            out[k] = v

        return out


def as_date(dat):
    """Return the RFC3339 UTC string representation of the given date and time.

    Args:
        dat (:py:class:`datetime.date`): the object/type to be serialized.

    Raises:
        TypeError:
            when ``o`` is not an instance of ``datetime.date``.

    Returns:
        (str) JSON serializable type for the given object.
    """
    LOGGER.debug('as_date(%s)', dat)

    return strict_rfc3339.timestamp_to_rfc3339_utcoffset(
        calendar.timegm(dat.timetuple()))
