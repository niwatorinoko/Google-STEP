from collections import defaultdict



def solution(input_word):
    sorted_word = "".join(sorted(input_word))

    word_file = open("anagram/words.txt", "r")
    words = word_file.readlines()
    word_file.close()

    new_dictionary = defaultdict(list)
    for word in words:
        word = word.strip()
        if len(word) == len(sorted_word) and word != input_word:
            new_dictionary["".join(sorted(word))].append(word)
    return new_dictionary[sorted_word]

# input_word = input("Please input word : ")
# print(solution(input_word))
