import tests


class ATestCase(tests.BaseTestCase):

    def test(self):
        self.assertTrue(self.logging_loaded)
        self.assertTrue(self.configuration_loaded)

        self.assertFalse(self.logger is not None)

        self.assertFalse(self.configuration is not None)
        self.assertEquals(self.configuration['company.package']['key'], 'value')
