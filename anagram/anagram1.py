from collections import defaultdict

def dictionary_to_list():
    fname = "anagram/words.txt"
    with open(fname,"r") as file:
        dictionary_words = file.read().splitlines()
    return dictionary_words


def find_anagram(input_word, dict_words):
    #sorted_input_word = "".join(sorted(input_word))
    # new_dict = defaultdict(list)
    # for dict_word in dict_words:
    #     if len(dict_word) == len(sorted_input_word) and dict_word != input_word:
    #         new_dict["".join(sorted(dict_word))].append(dict_word)
    # return new_dict[sorted_input_word]
    input_word = input_word.replace(" ", "")
    new_dict = defaultdict(list)
    input_word_count = [0] * 26
    for c in input_word:
        if not ('a' <= c <= 'z'):
            return []
        input_word_count[ord(c) - ord("a")] += 1
    input_word_count = tuple(input_word_count)

    for dict_word in dict_words:
        count = [0] * 26
        for c in dict_word:
            count[ord(c) - ord("a")] += 1
        new_dict[tuple(count)].append(dict_word)
    return new_dict[input_word_count]


def binary_search(dict, word):
    anagram = []
    l, r = 0, len(dict)-1
    while l <= r:
        mid = (l+r) // 2
        if dict[mid][0] == word:
            anagram.append(dict[mid][1])
            l = mid - 1
            r = mid + 1
            while dict[l][0] == word and l >= 0:
                anagram.append(dict[l][1])
                l -= 1
            while dict[r][0] == word and r < len(dict):
                anagram.append(dict[r][1])
                r += 1
            return anagram
        elif dict[mid][0] < word:
            l = mid + 1
        elif dict[mid][0] > word:
            r = mid - 1
    return []


def find_anagram_by_binary_search(input_word, dict_words):
    input_word = input_word.replace(" ", "")
    sorted_input_word = "".join(sorted(input_word))

    new_dict = []
    for dict_word in dict_words:
        #[辞書のソートされた単語, 辞書の単語]
        new_dict.append(["".join(sorted(dict_word)),dict_word])
    new_dict = sorted(new_dict)

    return binary_search(new_dict, sorted_input_word)


# print(find_anagram("lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoio", dictionary_to_list()))
# print(find_anagram_by_binary_search("lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphioparaomelitokatakechymenokichlepikossyphophattoperisteralektryonoptekephalliokigklopeleiolagoio", dictionary_to_list()))