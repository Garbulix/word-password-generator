import random

class WordDictionary():
    """class with words loaded from specified and prepared file. Aimed to be read-only"""

    def __init__(self, path = ''):

        self._words = []

        if path != '':
            try:
                with open(path) as dict_file:
                    all_file_lines = dict_file.read().splitlines()
                    for line in all_file_lines:
                        # toss all lines starting with '#'
                        if line[0] == '#':
                            continue
                        else:
                            self._words.append(line)
            except FileNotFoundError:
                print('ERROR: Dictionary file not found, sorry!')
                raise SystemExit()

    def __getitem__(self, index):
        """overload [] operator - only for getting word under given index"""
        return self._words[index]

    def __len__(self):
        """return number of _words in dictionary"""
        return len(self._words)

    def clear(self):
        """clears/resets the container"""
        self._words.clear()