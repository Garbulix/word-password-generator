import random
import WordDictionary


class WordPassword():
    def __init__(self, dictionary=WordDictionary(), no_of_words=0, capitalize=False, separator='-', numbers_to_insert=0):
        self.dictionary = dictionary
        self.no_of_words = no_of_words
        self.capitalize = capitalize
        self.separator = separator
        self.numbers_to_insert = numbers_to_insert

        if len(dictionary) > 0:
            # create first password 
            pass

    def regenerate_password(self):
        random.seed()
        

