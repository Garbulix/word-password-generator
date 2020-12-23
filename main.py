import sys
import Password
import WordDictionary

"""
TODO class and method comments
"""

cli_arguments = sys.argv[:]

# CONFIGS #
WORDS_IN_PASS = int(cli_arguments[1])
SEPARATOR = cli_arguments[2]
CAPITALIZE = bool(cli_arguments[3])
NUMBERS_TO_INSERT = int(cli_arguments[4])
PATH = '/home/bartek/Programowanie/word-password-generator/dictionaries/RANDOM.txt'
# CONFIGS #

# ===================================
dictionary = WordDictionary.WordDictionary(PATH)
sample_password = Password.WordPassword(dictionary, WORDS_IN_PASS, CAPITALIZE, SEPARATOR, NUMBERS_TO_INSERT)
print(sample_password.password)