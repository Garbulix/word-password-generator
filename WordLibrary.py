import random

class WordLibrary():
    """class with words loaded from given file"""

    def __init__(self, path = ''):
        self.is_imported = False
        self.dictionary_name = ''
        self.words = []

        if path != '':
            with open(path) as dict_file:
                self.words = dict_file.read().splitlines()
                self.is_imported = True
                self.dictionary_name = self.words[0]
                self.words = self.words[2:]     # get rid of dict name and '#' line

