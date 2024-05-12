import unittest

from anagram1 import solution


class TestAnagram1(unittest.TestCase):
    def test_should_return_None_if_input_is_empty(self):
        anagram = solution("")
        self.assertEqual([], anagram)

    def test_should_return_empty_list_if_dictionary_is_empty(self):
        anagram = solution("act")
        self.assertEqual(["cat"], anagram)

if __name__ == '__main__':
    unittest.main()