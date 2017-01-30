import mock
import unittest

# Test file should start with test_
# Test class should start with Test
# Test methods should start with test_


# List of all assert*, taken from https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertEqual
# assertEqual(a, b)
# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIs(a, b)
# assertIsNot(a, b)
# assertIsNone(x)
# assertIsNotNone(x)
# assertIn(a, b)
# assertNotIn(a, b)
# assertIsInstance(a, b)
# assertIsNotInstance(a, b)
class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_is(self):
        self.assertIsNot(0, False)
        self.assertIs(1 == 1, True)

    def test_list(self):
        self.assertIn("a", ["b", "c", "a"])
        self.assertNotIn("fsadf", ["dsf", "df"])

    def test_mock(self):
        mock_test = mock.Mock()
        dummy_func(mock_test)
        mock_test.test456test.assert_called_once_with()


# This dummy function accepts an object an calls the method test456test of this object
def dummy_func(obj):
    obj.test456test()
