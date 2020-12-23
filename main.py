import sys
import Password
import WordDictionary

"""
TODO class and method comments
"""

# CLI arguments #
cli_arguments = sys.argv[:]
DICT_PATH = cli_arguments[1]
WORDS_IN_PASS = int(cli_arguments[2])
SEPARATOR = cli_arguments[3]
CAPITALIZE = bool(cli_arguments[4])
NUMBERS_TO_INSERT = int(cli_arguments[5])
# CLI arguments #

# ===================================
dictionary = WordDictionary.WordDictionary(DICT_PATH)
sample_password = Password.WordPassword(dictionary, WORDS_IN_PASS, CAPITALIZE, SEPARATOR, NUMBERS_TO_INSERT)
print(sample_password.password)