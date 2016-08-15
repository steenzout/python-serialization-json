# -*- coding: utf-8 -*-
"""
Test cases for the steenzout.serialization.json package.
"""

import calendar
import strict_rfc3339
import unittest

from datetime import date, datetime

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
        self.assertEqual(t, json.deserialize('"%s"' % t_rfc3339))

    def test_deserialize_object(self):
        """Test deserialize() function."""
        class A:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        a = A(1, 2)
        self.assertEqual(a, json.deserialize('{"x": 1, "y": 2}', cls=A))

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

        class A:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        a = A(1, 2)
        self.assertEqual('{"x": 1, "y": 2}', json.serialize(a))
