import tests
import unittest


class ATestCase(unittest.TestCase, tests.Basic):

    def setUp(self):
        self.setup_configuration()
        self.setup_logger('%s.%s' % (__name__, ATestCase.__name__))

    def test(self):
        self.assertTrue(self.logging_loaded)
        self.assertTrue(self.logging_loaded)

        self.logger.debug('test()')
