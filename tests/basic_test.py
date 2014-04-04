import tests
import unittest


class ATestCase(unittest.TestCase, tests.Basic):

    def setUp(self):
        self.setup_configuration()
        self.setup_logger()

    def test(self):
        self.assertTrue(self.logging_loaded)
        self.assertTrue(self.logging_loaded)

        self.assertFalse(self.logger is not None)

        self.assertFalse(self.configuration is not None)
        self.assertEquals(self.configuration['company.package']['key'], 'value')
