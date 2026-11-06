import unittest
from core.utils import get_current_time


class UtilsTests(unittest.TestCase):
    def test_current_time_returns_text(self):
        result = get_current_time()
        self.assertIsInstance(result, str)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
