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
.. module:: steenzout.serialization.json
    :synopsis: JSON serialization/deserialization package.

.. moduleauthor:: Pedro Salgado <steenzout@ymail.com>
"""

import datetime
import simplejson
import six

from . import encoders
from .version import __version__


SerializationMapping = {
    object: {
        'default': encoders.as_object,
        'sort_keys': True
    },
    datetime.date: {
        'default': encoders.as_date
    }
}


def serialize(o):
    """
    Serializes the given object into JSON.

    :param o: the object/type to be serialized.

    :return: JSON representation of the given object/type.
    :rtype: str
    """

    kwargs = {'default': None}
    for t, args in six.iteritems(SerializationMapping):
        if isinstance(o, t):
            kwargs = args
            break

    return simplejson.dumps(o, **kwargs)


def deserialize(json, cls=None):
    """
    Deserializes a JSON string into a Python object or type.

    :param json: the JSON string.
    :type json: str
    :param cls: if the ``jsonstr`` is deserialized into a ``dict`` and
                this argument is set,
                the ``dict`` keys are passed as keyword arguments to the
                given ``cls`` initializer.
    :type cls: classobj

    :return: Python object/type representation of the given object.
    """
    out = simplejson.loads(json)

    if isinstance(out, dict) and cls is not None:
        return cls(**out)

    return out
