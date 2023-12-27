# import unittest
import pytest

from main import is_palindrome, Database


# def setUpModule():
#     pass
#
#
# def tearDownModule():
#     pass


# class MainTestCase(unittest.TestCase):
#
#     def test_is_palindrome(self):
#         self.assertFalse(is_palindrome("qwerqwer"))


# class DatabaseTestCase(unittest.TestCase):
#     instance = None
#
#     @classmethod
#     def setUpClass(cls):
#         cls.instance = Database()
#         print("DONE")
#
#     @unittest.expectedFailure
#     def test_get(self):
#         self.assertIsNotNone(self.instance.get(4))
#
#     def test_delete(self):
#         self.assertIsNone(self.instance.delete(2))


@pytest.fixture()
def foo():
    return 1234


@pytest.mark.asyncio
@pytest.mark.parametrize(
    argnames=("text", "result"), argvalues=((1234, False), ("qwewq", True))
)
async def test_is_palindrome(text, result):
    a = is_palindrome(text)
    assert a == result
