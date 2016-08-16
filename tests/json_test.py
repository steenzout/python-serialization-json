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
Test cases for the steenzout.serialization.json package.
"""

import calendar
import strict_rfc3339
import unittest

from datetime import date, datetime

from steenzout.object import Object
from steenzout.serialization import json


class PackageTestCase(unittest.TestCase):
    """Test case for the json package function()."""

    def test_deserialize(self):
        """Test deserialize() function."""

        self.assertEqual(1, json.deserialize('1'))
        self.assertEqual({'a': 1}, json.deserialize('{"a": 1}'))

    def test_deserialize_date(self):
        """Test deserialize() function."""

        t = datetime(2016, 8, 15, 12, 0, 1, 999999)  # in UTC
        t_rfc3339 = strict_rfc3339.timestamp_to_rfc3339_utcoffset(
            calendar.timegm(t.timetuple())
        )
        self.assertEqual('2016-08-15T12:00:01Z', json.deserialize('"%s"' % t_rfc3339))

    def test_deserialize_object(self):
        """Test deserialize() function."""
        class A(Object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        a = A(1, 2)
        self.assertEqual(a, json.deserialize('{"x": 1, "y": 2}', cls=A))

    def test_deserialize_other(self):
        """Test serialize() function."""

        self.assertEqual(1, json.deserialize('1'))

    def test_serialize_date(self):
        """Test serialize() function."""

        dt = date(2016, 8, 15)  # in UTC
        dt_rfc3339 = strict_rfc3339.timestamp_to_rfc3339_utcoffset(
            calendar.timegm(dt.timetuple())
        )
        self.assertEqual('"%s"' % dt_rfc3339, json.serialize(dt))

    def test_serialize_datetime(self):
        """Test serialize() function."""

        t = datetime(2016, 8, 15, 12, 0, 1, 999999)  # in UTC
        t_rfc3339 = strict_rfc3339.timestamp_to_rfc3339_utcoffset(
            calendar.timegm(t.timetuple())
        )
        self.assertEqual('"%s"' % t_rfc3339, json.serialize(t))

    def test_serialize_object(self):
        """Test serialize() function."""

        class A(Object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        result = json.serialize(A(1, 2))
        self.assertTrue(
            '{"x": 1, "y": 2}' == result or
            '{"y": 2, "x": 1}' == result
        )

    def test_serialize_other(self):
        """Test serialize() function."""

        self.assertEqual('1', json.serialize(1))
