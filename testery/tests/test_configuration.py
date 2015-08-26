import os

from paste.deploy.loadwsgi import appconfig

from testery.tests import TestCase


class TestConfiguration(TestCase):
    """Check that the ini files track the same configuration types."""

    def setUp(self):
        super(TestConfiguration, self).setUp()
        here = os.path.dirname(__file__)
        self.project_root = os.path.abspath(os.path.join(here, '..', '..'))

    def test_development_ini(self):
        test_ini = os.path.join(self.project_root, 'test.ini')
        test_settings = appconfig('config:' + test_ini)
        dev_ini = os.path.join(self.project_root, 'development.ini')
        dev_settings = appconfig('config:' + dev_ini)
        self.assertEqual(test_settings.keys(), dev_settings.keys())
