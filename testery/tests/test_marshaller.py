from testery import marshaller, models
from testery.tests import TestCase


class TestMarshaller(TestCase):

    def test_marshall_build_collection(self):
        build_1 = self.factory.make_build(passes=1, fails=2, skips=3)
        build_2 = self.factory.make_build(passes=4, fails=5, skips=6)

        marshalled = marshaller.marshall(models.Build, [build_1, build_2])

        expected = {
            'builds': [{
                'id': build_1.id,
                'passes': build_1.passes,
                'fails': build_1.fails,
                'skips': build_1.skips,
            }, {
                'id': build_2.id,
                'passes': build_2.passes,
                'fails': build_2.fails,
                'skips': build_2.skips,
            }]
        }
        self.assertEqual(expected, marshalled)
