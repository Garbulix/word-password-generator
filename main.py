import word_generator
import random

"""
TODO:
- make config file or take configs from CLI arguments
- GUI
- make directory with words library
"""

# CONFIGS #
WORDS_IN_PASS = 4
SEPARATOR = '-'
MIN_WORD_LENGTH = 4
MAX_WORD_LENGTH = 7
CAPITALIZE = True
PUT_NUMBER_SOMEWHERE = True
NO_OF_NUMBERS_TO_PUT = 6
# CONFIGS #

no_of_separators = WORDS_IN_PASS - 1
words_to_use = word_generator.generate_word_list(WORDS_IN_PASS, MIN_WORD_LENGTH, MAX_WORD_LENGTH)
random.seed()

def generate_password():
    if PUT_NUMBER_SOMEWHERE:
        # add a random numbers after a random words
        for number in range(NO_OF_NUMBERS_TO_PUT):
            randomly_chosen_word_index = random.randint(0, len(words_to_use) - 1)
            words_to_use[randomly_chosen_word_index] += str(random.randint(0, 9))

    if CAPITALIZE:
        words_to_use_capitalized = [word.capitalize() for word in words_to_use]
        return SEPARATOR.join(words_to_use_capitalized)
    else:
        return SEPARATOR.join(words_to_use)

# ===================================

print(generate_password())