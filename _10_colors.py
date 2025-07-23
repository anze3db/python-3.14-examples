# Type in the PyRepl:


# class Hello:
#     print("holla")

# python -m json test.json

# python -m calendar

# Colors in argparse!
import argparse

prameters = argparse.ArgumentParser(description="A simple test script.")
prameters.add_argument("--name", type=str, help="Name of the person to greet.")
args = prameters.parse_args()

# Colors in unittest!
from unittest import TestCase


class TestHello(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_failure(self):
        self.assertTrue(False)
