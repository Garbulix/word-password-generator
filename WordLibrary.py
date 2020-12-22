import random

class WordLibrary():
    """class with words loaded from given file"""

    def __init__(self, path = ''):
        self.is_imported = False
        self.dictionary_name = ''
        self.words = []

        if path != '':
            try:
                with open(path) as dict_file:
                    self.words = dict_file.read().splitlines()
                    self.is_imported = True
                    self.dictionary_name = self.words[0]
                    self.words = self.words[2:]     # toss dict name and '#' line
            except IOError:
                print('File not found, sorry!')

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def clear(self):
        self.words.clear()