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
"""JSON serialization package."""

import datetime
import logging
import simplejson

from . import encoders
from .metadata import __version__


LOGGER = logging.getLogger('steenzout.serialization.json')


def serialize(obj):
    """Serialize the given object into JSON.

    Args:
        obj: the object to be serialized.

    Returns:
        (str): JSON representation of the given object.
    """
    LOGGER.debug('serialize(%s)', obj)

    if isinstance(obj, datetime.date):
        return simplejson.dumps(obj, default=encoders.as_date)

    elif hasattr(obj, '__dict__'):
        return simplejson.dumps(obj, default=encoders.as_object)

    return simplejson.dumps(obj)


def deserialize(json, cls=None):
    """Deserialize a JSON string into a Python object.

    Args:
        json (str): the JSON string.
        cls (:py:class:`object`):
            if the ``json`` is deserialized into a ``dict`` and
            this argument is set,
            the ``dict`` keys are passed as keyword arguments to the
            given ``cls`` initializer.

    Returns:
        Python object representation of the given JSON string.
    """
    LOGGER.debug('deserialize(%s)', json)

    out = simplejson.loads(json)

    if isinstance(out, dict) and cls is not None:
        return cls(**out)

    return out


def version():
    """Return this package version.

    Returns:
        (str): package version.
    """
    return __version__
