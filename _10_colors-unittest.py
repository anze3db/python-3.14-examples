from unittest import TestCase


class TestHello(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_failure(self):
        self.assertTrue(False)
