import unittest

from anagram1 import find_anagram, dictionary


class TestAnagram1(unittest.TestCase):
    #inputが空の場合、空を返すか。
    def test_should_return_None_if_input_is_empty(self):
        anagram = find_anagram("", dictionary())
        assert anagram == []


    #辞書が空の場合、空を返すか。
    def test_should_return_empty_list_if_dictionary_is_empty(self):
        anagram = find_anagram("act", [])
        assert anagram == []

    
    #tcaが入力された場合、catとactを返すか。
    def test_should_return_cat_and_act(self):
        anagram = find_anagram("tca", dictionary())
        assert "cat" in anagram
        assert "act" in anagram

    #
    def test_should_return_cat_and_act_with_spaced_input_string(self):
        anagram = find_anagram("t ca", dictionary())
        assert anagram == []


    def test_should_return_empty_if_word_too_long(self):
        anagram = find_anagram("lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoio-siraiobaphetraganopterygon", dictionary())
        assert anagram == []


if __name__ == '__main__':
    unittest.main()