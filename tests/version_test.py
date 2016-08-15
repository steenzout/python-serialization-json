# -*- coding: utf-8 -*-

import unittest


class VersionTestCase(unittest.TestCase):
    """
    Test case for the version module.
    """

    def test_attributes(self):
        """
        Tests the version module attributes.
        """
        from steenzout.serialization.json import version

        self.assertFalse(version.__dict__ is None)
        self.assertTrue('__version__' in version.__dict__)
