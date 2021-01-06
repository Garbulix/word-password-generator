import unittest
import random

from Password import WordPassword
import WordDictionary as wd

class TestWordPassword(unittest.TestCase):

    def setUp(self, no_of_words=5, capitalize=True, separator='-', numbers_to_insert=1):
        self.test_dict_path = './test_files/RANDOM.txt'
        self.test_dict = wd.WordDictionary(self.test_dict_path)
        self.test_password = WordPassword(self.test_dict, no_of_words, capitalize, separator, 
            numbers_to_insert)
        self.number_of_tests = 100

    def test_no_of_words(self):
        """testing wheter number of words is correct"""
        random.seed()
        min_words = 3
        max_words = 15

        for i in range(self.number_of_tests):
            random_number = random.randint(min_words, max_words)
            self.setUp(no_of_words=random_number)
            used_separator = self.test_password.separator
            words = self.test_password.password.split(used_separator)

            self.assertEqual(random_number, len(words))
        
    def test_no_of_numbers(self):
        """test if there are requested number of digits"""
        random.seed()
        min_digits = 1
        max_digits = 100
        exact_digits_occur = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0
        }

        for i in range(self.number_of_tests):
            random_number = random.randint(min_digits, max_digits)
            self.setUp(numbers_to_insert=random_number)
            for digit in range(0, 10):
                # count occurs of exact digits
                exact_digits_occur[digit] = self.test_password.password.count(str(digit))
            all_occurences = sum(exact_digits_occur.values())
            
            self.assertEqual(all_occurences, random_number)

# ----------

if __name__ == '__main__':
    unittest.main()