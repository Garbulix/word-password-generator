import unittest

import WordDictionary as wd

class TestWordDictionary(unittest.TestCase):
    default_file = {
        "path": "./test_files/1-1.txt",
        "no_of_comments": 1,
        "no_of_words": 1}
    test_files=[
        {"path": "./test_files/0-0.txt",
        "no_of_comments": 0,
        "no_of_words": 0},
        {"path": "./test_files/7020-0.txt",
        "no_of_comments": 7020,
        "no_of_words": 0},
        {"path": "./test_files/23-44.txt",
        "no_of_comments": 23,
        "no_of_words": 44},
        {"path": "./test_files/29-0.txt",
        "no_of_comments": 29,
        "no_of_words": 0},
        {"path": "./test_files/7020-4943.txt",
        "no_of_comments": 7020,
        "no_of_words": 4943},
        {"path": "./test_files/0-5568.txt",
        "no_of_comments": 0,
        "no_of_words": 5568},
        ]

    def setUp(self, optional_file_index=-1):
            if optional_file_index == -1:
                self.dictionary = wd.WordDictionary(self.default_file["path"])
            else:
                self.dictionary = wd.WordDictionary(self.test_files[optional_file_index]["path"])

    def test_loading_file(self):
        """test whether (number of loaded words) == (number of uncommented lines in file)"""
        for file_index in range(len(self.test_files)):
            print("testing file: " + self.test_files[file_index]["path"])
            self.setUp(file_index)
            self.assertEqual(len(self.dictionary), self.test_files[file_index]["no_of_words"])

# ----------

if __name__ == "__main__":
    unittest.main()