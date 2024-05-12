from collections import Counter,defaultdict

DICTIONARY_COUNT = defaultdict(dict)
def dictionary_words_counter():
    word_file = open("anagram/words.txt", "r")
    words = word_file.readlines()
    word_file.close()

    for word in words:
        word = word.strip()
        word_counter = Counter(word)
        DICTIONARY_COUNT[word] = word_counter

def solution(input_word):
    input_word_counter = Counter(input_word)

    ans = ["", 0]
    for word, counter in DICTIONARY_COUNT.items():
        if counter <= input_word_counter:
            if ans[1] < max(ans[1], word_score_calculator(word)):
                ans = [word, word_score_calculator(word)]
    return ans

def word_score_calculator(word):
    score = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    word_score = 0
    for s in word:
        word_score += score[ord(s)-97]
    return word_score

def small_count():
    small_text_file = open("anagram/small.txt", "r")
    small_words = small_text_file.readlines()
    small_text_file.close()
    for small_word in small_words:
        small_word = small_word.strip()
        print(solution(small_word)[0])

def medium_count():
    medium_text_file = open("anagram/medium.txt", "r")
    medium_words = medium_text_file.readlines()
    medium_text_file.close()
    for medium_word in medium_words:
        medium_word = medium_word.strip()
        print(solution(medium_word)[0])

def large_count():
    large_text_file = open("anagram/large.txt", "r")
    large_words = large_text_file.readlines()
    large_text_file.close()

    large_text_answer_file = open("anagram/large_answer.txt", "w")

    for large_word in large_words:
        large_word = large_word.strip()
        large_text_answer_file.write(solution(large_word)[0] + "\n")

if __name__ == '__main__':
    dictionary_words_counter()
    #small_count()
    #medium_count()
    large_count()