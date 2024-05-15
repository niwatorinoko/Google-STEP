import unittest

from anagram1 import find_anagram, dictionary_to_list


class TestAnagram(unittest.TestCase):
    

    def test_should_return_None_if_input_is_empty(self):
        anagram = find_anagram("", dictionary_to_list())
        assert anagram == []


    def test_should_return_empty_list_if_dictionary_is_empty(self):
        anagram = find_anagram("act", [])
        assert anagram == []

    
    def test_should_return_many_words(self):
        anagram = find_anagram("stop", dictionary_to_list())
        assert "post" in anagram
        assert "opts" in anagram
        assert "pots" in anagram
        assert "spot" in anagram
        assert "tops" in anagram


    def test_should_return_empty_with_spaced_input_string(self):
        anagram = find_anagram("t ca", dictionary_to_list())
        assert anagram == []


    def test_should_return_empty_if_word_too_long(self):
        anagram = find_anagram("lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoio-siraiobaphetraganopterygon", dictionary_to_list())
        assert anagram == []
    
    
    def test_should_return_empty_if_word_too_short(self):
        anagram = find_anagram("j", dictionary_to_list())
        assert anagram == []


    def test_should_return_empty_if_word_has_special_char(self):
        anagram = find_anagram("あいうえおかきくけこ", dictionary_to_list())
        assert anagram == []

    
    def test_should_return_one_word(self):
        anagram = find_anagram("cat", dictionary_to_list())
        assert anagram == ["act"]


    def test_should_return_empty_if_no_anagram(self):
        anagram = find_anagram("image", dictionary_to_list())
        assert anagram == []

if __name__ == '__main__':
    unittest.main()