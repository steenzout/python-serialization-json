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
"""Unit tests for the version module."""

import unittest


class VersionTestCase(unittest.TestCase):
    """
    Test case for the version module.
    """

    def test_attributes(self):
        """
        Tests the version module attributes.
        """
        import steenzout.serialization.json

        self.assertTrue(
            steenzout.serialization.json.version() == steenzout.serialization.json.__version__
        )
