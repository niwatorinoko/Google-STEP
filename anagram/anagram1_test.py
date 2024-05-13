import unittest

from anagram1 import solution


class TestAnagram1(unittest.TestCase):
    #inputが空の場合、空を返すか。
    def test_should_return_None_if_input_is_empty(self):
        anagram = solution("")
        assert anagram == []

    #辞書が空の場合、空を返すか。
    def test_should_return_empty_list_if_dictionary_is_empty(self):
        anagram = solution("act")
        assert anagram == ["cat"]
    
    #tcaが入力された場合、catとactを返すか。
    def test_should_return_cat_and_act(self):
        anagram = solution("tca")
        assert "cat" in anagram
        assert "act" in anagram

    #
    def test_should_return_cat_and_act_with_spaced_input_string(self):
        anagram = solution("t ca")
        assert anagram == []

    def test_should_return_empty_if_word_too_long(self):
        anagram = solution("Lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoio-siraiobaphetraganopterygon")
        assert anagram == []

if __name__ == '__main__':
    unittest.main()