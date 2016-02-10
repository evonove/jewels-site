from django.test import TestCase


class SimpleTestCase(TestCase):
    def setUp(self):
        pass

    def test_simple_empty_test(self):
        """
        This test is used as a placeholder so you can immediately
        test your CI integration
        """
        self.assertEqual(1, 1)

    def test_simple_empty_test_failure(self):
        """
        This test is used as a placeholder so you can immediately
        test your CI integration
        """
        self.assertEqual(0, 1)
