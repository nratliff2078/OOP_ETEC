from unittest import TestCase

class T(TestCase):
    def test_dummy(self):
        self.assertEqual(1,1)   # 1 == 1
    def test_shouldFail(self):
        self.assertEqual(0,0)  # will fail if 1,0 or 0,1