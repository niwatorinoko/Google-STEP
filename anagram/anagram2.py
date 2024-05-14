from collections import Counter,defaultdict


def find_highest_score_anagram(input_word):
    dictionary_words_counter()

    input_word_counter = Counter(input_word)
    
    curr_word = ""
    curr_score = 0
    #[現在の一番ハイスコアな単語, スコア]
    #ans = ["", 0]
    for dict_word, counter in DICTIONARY_COUNT.items():
        if counter <= input_word_counter:
            if curr_score < max(curr_score, word_score_calculator(dict_word)):
                curr_word = dict_word
                curr_score = max(curr_score, word_score_calculator(dict_word))
    return curr_word


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


def write_high_score_anagram(problem_file, answer_file):
    with open(problem_file, "r") as file:
        words = file.read().splitlines()    

    with open(answer_file, "w") as file:
        for word in words:
            file.write(find_highest_score_anagram(word) + "\n")


# if __name__ == '__main__':
#     write_high_score_anagram("anagram/small.txt", "anagram/small_answer.txt")
#     write_high_score_anagram("anagram/medium.txt", "anagram/medium_answer.txt")
#     write_high_score_anagram("anagram/large.txt", "anagram/large_answer.txt")
#     print(find_highest_score_anagram("funseseldenessse"))