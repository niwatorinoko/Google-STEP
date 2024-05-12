import unittest

from anagram1 import solution


class TestAnagramPart1(unittest.TestCase):
    def test_should_return_None_if_input_is_empty(self):
        anagram = solution("", ["act"])
        assert anagram == None


    def test_should_return_empty_list_if_dictionary_is_empty(self):
        anagram = solution("act", [])
        assert anagram == []


    def test_should_return_cat_and_act(self):
        anagram = solution("tca", ["cat", "act", "ac"])
        assert "cat" in anagram
        assert "act" in anagram


    def test_should_return_cat_and_act_with_spaced_input_string(self):
        anagram = solution("t ca", ["cat", "act"])
        assert "cat" in anagram
        assert "act" in anagram


    def test_should_return_empty_list_if_sorted_input_string_not_exist_in_dictionary(self):
        words = solution("words.txt")
        anagram = solution("aqz", words)
        assert anagram == []


if __name__ == '__main__':
    unittest.main()