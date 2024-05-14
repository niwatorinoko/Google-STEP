from collections import Counter,defaultdict


def find_highest_score_anagram(input_word):
    input_word_counter = Counter(input_word)

    ans = ["", 0]
    for dict_word, counter in DICTIONARY_COUNT.items():
        if counter <= input_word_counter:
            if ans[1] < max(ans[1], word_score_calculator(dict_word)):
                ans = [dict_word, word_score_calculator(dict_word)]
    return ans


def word_score_calculator(word):
    score = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    word_score = 0
    for s in word:
        word_score += score[ord(s)-97]
    return word_score


DICTIONARY_COUNT = defaultdict(dict)
def dictionary_words_counter():
    word_file = open("anagram/words.txt", "r")
    words = word_file.readlines()
    word_file.close()

    for word in words:
        word = word.strip()
        word_counter = Counter(word)
        DICTIONARY_COUNT[word] = word_counter


def small_text_score_count():
    fname = open("anagram/small.txt", "r")
    with open(fname,"r") as file:
        words = file.read().splitlines()    

    small_text_answer_file = open("anagram/small_answer.txt", "w")
    for small_word in words:
        small_text_answer_file.write(find_highest_score_anagram(small_word)[0] + "\n")


def medium_text_score_count():
    fname = open("anagram/medium.txt", "r")
    with open(fname,"r") as file:
        words = file.read().splitlines()    

    medium_text_answer_file = open("anagram/medium_answer.txt", "w")
    for medium_word in words:
        medium_text_answer_file.write(find_highest_score_anagram(medium_word)[0] + "\n")


def large_text_score_count():
    fname = open("anagram/large.txt", "r")
    with open(fname,"r") as file:
        words = file.read().splitlines()    

    large_text_answer_file = open("anagram/large_answer.txt", "w")
    for large_word in words:
        large_text_answer_file.write(find_highest_score_anagram(large_word)[0] + "\n")


#if __name__ == '__main__':
    #dictionary_words_counter()
    #small_count()
    #medium_count()
    #large_count()