# test_app.py
import unittest

class TestApp(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2, "სიმულირებული ჩავარდნა CI/CD პაიპლაინში")
