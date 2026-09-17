import unittest
from utils import utils


class TestUtils(unittest.TestCase):
    @staticmethod
    def test_reversed_integer():
        assert utils.reversed(123) == 321

    @staticmethod
    def test_reversed_string():
        try:
            utils.reversed("123")
            assert False
        except TypeError:
            pass

    @staticmethod
    def test_reversed_float():
        try:
            utils.reversed(12.3)
            assert False
        except TypeError:
            pass

    @staticmethod
    def test_formatter_integer():
        assert utils.formatter(10) == ("0b1010", "0o12")

    @staticmethod
    def test_formatter_string():
        try:
            utils.formatter("10")
            assert False
        except TypeError:
            pass

    @staticmethod
    def test_formatter_float():
        try:
            utils.formatter(10.5)
            assert False
        except TypeError:
            pass

if __name__ == "__main__":
    unittest.main()