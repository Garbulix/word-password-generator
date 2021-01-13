import random

class WordDictionary():
    """class with words loaded from specified, prepared file. 
    Works similarly to list. Aimed to be read-only"""

    def __init__(self, path = ""):
        """import words from wordfile in path.
        Object can be made without path - then it will be empty"""

        self._words = []
        
        if len(path):
            self.import_from_file(path)

    def __getitem__(self, index):
        """overload [] operator - only for getting word under given index"""
        return self._words[index]

    def __len__(self):
        """return number of words in dictionary"""
        return len(self._words)

    def import_from_file(self, path=""):
        """import new wordfile. Clears existing words."""
        self.clear()

        try:
            with open(path) as dict_file:
                all_file_lines = dict_file.read().splitlines()
                for line in all_file_lines:
                    # toss all lines starting with "#"
                    if line[0] == "#":
                        continue
                    else:
                        self._words.append(line)
        except FileNotFoundError:
            print("ERROR: Dictionary file not found, sorry!")
            raise SystemExit()

    def clear(self):
        """clears/resets the container"""
        self._words.clear()

    def return_wordlist(self):
        """return copy of the list with all words"""
        return self._words[:]