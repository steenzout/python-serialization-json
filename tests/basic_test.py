import tests


class ATestCase(tests.BaseTestCase):

    def test_logging_configuration_loaded(self):
        self.assertTrue(self.logger is not None)

    def test_configuration_loaded(self):
        self.assertTrue(self.configuration is not None)

    def test_configuration_contents(self):
        self.assertEquals(self.configuration['company.package']['key'], 'value')
