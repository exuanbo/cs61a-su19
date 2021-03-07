""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"


def lines_from_file(path):
    with open(path) as file:
        assert file.readable() == True
        return [line.strip() for line in file.readlines()]


def new_sample(path, i):
    lines = lines_from_file(path)
    return lines[i]


def get_typed_words_per_minute(typed_string, start_time, end_time):
    approximate_typed_words_count = len(typed_string) / 5
    return (approximate_typed_words_count / (end_time - start_time)) * 60


def get_accuracy_percentage(sample_paragraph, typed_string):
    word_list = sample_paragraph.split()
    typed_word_list = typed_string.split()
    typed_words_count = len(typed_word_list)
    if typed_words_count == 0:
        return 0.0
    min_words_count = min(len(word_list), typed_words_count)
    errors_count = sum([
        1 for i in range(min_words_count) if word_list[i] != typed_word_list[i]
    ])
    return ((min_words_count - errors_count) / min_words_count) * 100


def analyze(sample_paragraph, typed_string, start_time, end_time):
    typed_words_per_minute = get_typed_words_per_minute(
        typed_string, start_time, end_time)
    accuracy_percentage = get_accuracy_percentage(sample_paragraph,
                                                  typed_string)
    return [typed_words_per_minute, accuracy_percentage]


def is_char_vowel(char):
    return char in ["a", "e", "i", "o", "u"]


def find_first_vowel_index(word):
    for char_index, char in enumerate(word):
        if is_char_vowel(char):
            return char_index


def pig_latin(word):
    if is_char_vowel(word[0]):
        return word + "way"
    first_vowel_index = find_first_vowel_index(word)
    consonant_cluster = word[:first_vowel_index]
    if consonant_cluster == word:
        return word + "ay"
    return word[first_vowel_index:] + consonant_cluster + "ay"


def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    difference_scores = [(word_index, score_function(user_input, word))
                         for word_index, word in enumerate(words_list)]
    word_index_with_min_score = min(difference_scores, key=lambda t: t[1])[0]
    return words_list[word_index_with_min_score]


def swap_score(word1, word2):
    if not word1 or not word2:
        return 0
    return (word1[0] != word2[0] and 1 or 0) + swap_score(word1[1:], word2[1:])


# END Q1-5

# Question 6


def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2.
    """
    if not word1 or not word2 or word1 in word2 or word2 in word1:
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return abs(len(word1) - len(word2))
        # END Q6

    elif word1[0] == word2[0]:
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return score_function(word1[1:], word2[1:])
        # END Q6

    else:
        add_char = 1 + score_function(word2[0] + word1, word2)
        remove_char = 1 + score_function(word1[1:], word2)
        substitute_char = 1 + score_function(word1[1:], word2[1:])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return min(add_char, remove_char, substitute_char)
        # END Q6


KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"


def score_function_accurate(word1, word2):
    if not word1 or not word2 or word1 in word2 or word2 in word1:
        return abs(len(word1) - len(word2))
    if word1[0] == word2[0]:
        return score_function_accurate(word1[1:], word2[1:])
    add_char = 1 + score_function_accurate(word2[0] + word1, word2)
    remove_char = 1 + score_function_accurate(word1[1:], word2)
    substitute_char = (KEY_DISTANCES[word1[0], word2[0]] +
                       score_function_accurate(word1[1:], word2[1:]))
    return min(add_char, remove_char, substitute_char)


def memoize(fn):
    cache = dict()

    def memoized_fn(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result

    return memoized_fn


def score_function_final(word1, word2):
    if not word1 or not word2 or word1 in word2 or word2 in word1:
        return abs(len(word1) - len(word2))
    if word1[0] == word2[0]:
        return score_function_final(word1[1:], word2[1:])
    add_char = 1 + score_function_final(word2[0] + word1, word2)
    remove_char = 1 + score_function_final(word1[1:], word2)
    substitute_char = (KEY_DISTANCES[word1[0], word2[0]] +
                       score_function_final(word1[1:], word2[1:]))
    return min(add_char, remove_char, substitute_char)


score_function_final = memoize(score_function_final)  # type: ignore

# END Q7-8
