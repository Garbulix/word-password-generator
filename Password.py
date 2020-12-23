import random
import WordDictionary as wd

class WordPassword():
    """container for password and their generator"""

    def __init__(self, dictionary=wd.WordDictionary(), no_of_words=0, 
                 capitalize=False, separator='-', numbers_to_insert=0):
        self.dictionary = dictionary
        self.no_of_words = no_of_words
        self.capitalize = capitalize
        self.separator = separator
        self.numbers_to_insert = numbers_to_insert
        
        self.password = ''
        self.is_generated = False

        if len(dictionary):
            self.regenerate_password()
            self.is_generated = True

    def regenerate_password(self):
        """(re)generate new password - randomly choose new words with every function call"""

        random.seed()
        available_words = len(self.dictionary)

        # randomly chose words to use without copying all dictionary
        drawn_words_indexes = random.sample(list(range(available_words)), self.no_of_words)
        words_to_use = [self.dictionary[word_index] for word_index in drawn_words_indexes]

        if self.capitalize:
            for word_index in range(len(words_to_use)):
                words_to_use[word_index] = words_to_use[word_index].capitalize()

        if self.numbers_to_insert:
            words_to_use_indexes = list(range(len(words_to_use)))
            words_to_put_numbers_to = random.choices(words_to_use_indexes, k=self.numbers_to_insert)
            for word_index in words_to_put_numbers_to:
                words_to_use[word_index] += str(random.randint(0, 9))
        
        self.password = self.separator.join(words_to_use)