import sys
import random
import WordLibrary

"""
TODO:
- make config file or take configs from CLI arguments
- GUI
- create word_generator as a submodule
- option do specify max word length
"""

cli_arguments = sys.argv[:]

# CONFIGS #
WORDS_IN_PASS = int(cli_arguments[1])
SEPARATOR = cli_arguments[2]
CAPITALIZE = bool(cli_arguments[3])
NUMBERS_TO_INSERT = int(cli_arguments[4])
PATH = '/home/bartek/Programowanie/word-password-generator/dictionaries/RANDOM.txt'
# TODO do I need random.seed()?
# CONFIGS #

# TODO clean that mess
def generate_password(word_dictionary, no_of_words):
    drawed_words = []
    dict_length = len(word_dictionary)

    for word in range(no_of_words):
        # TODO reject duplicates
        randomly_chosen_word_index = random.randint(0, dict_length - 1)
        drawed_words.append(word_dictionary[randomly_chosen_word_index])

    if NUMBERS_TO_INSERT > 0:
        # add a random numbers after a random words
        for number in range(NUMBERS_TO_INSERT):
            randomly_chosen_word_index = random.randint(0, len(drawed_words) - 1)
            drawed_words[randomly_chosen_word_index] += str(random.randint(0, 9))

    if CAPITALIZE:
        words_to_use_capitalized = [word.capitalize() for word in drawed_words]
        return SEPARATOR.join(words_to_use_capitalized)
    else:
        return SEPARATOR.join(drawed_words)

# ===================================

print(generate_password(WordLibrary.WordLibrary(PATH), WORDS_IN_PASS))