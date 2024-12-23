import unittest
from unittest import mock
from hrid import HRID

class TestGenerateFunction(unittest.TestCase):

    def setUp(self):
        self.hrid = HRID()
        self.hrid.delimiter = ', '
        self.hrid.random = mock.Mock()

    def test_string_elements_only(self):
        self.hrid.phrasefmt = ['hello', 'world']
        expected_output = 'hello, world'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_list_elements_only(self):
        self.hrid.phrasefmt = [['hello', 'hi'], ['world', 'earth']]
        self.hrid.random.choice.side_effect = ['hello', 'world']
        expected_output = 'hello, world'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_mixed_string_and_list_elements(self):
        self.hrid.phrasefmt = ['hello', ['world', 'earth'], 'again']
        self.hrid.random.choice.return_value = 'world'
        expected_output = 'hello, world, again'
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_empty_phrasefmt(self):
        self.hrid.phrasefmt = []
        expected_output = ''
        self.assertEqual(self.hrid.generate(), expected_output)

    def test_none_phrasefmt(self):
        self.hrid.phrasefmt = None
        with self.assertRaises(TypeError):
            self.hrid.generate()

if __name__ == '__main__':
    unittest.main()