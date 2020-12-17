# word generator from simple-apps-for-testing-purposes repository

import random

vowel = ['a', 'e', 'i', 'o', 'u', 'y']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'w', 'z']

def generate_word(length):
    # there is no word to create
    if length == 0:
        return ''
    
    generated_word = ''
    # randomly choose to start with vowel or consonant
    random.seed()
    start_with = random.choice(['vowel', 'consonant'])
    generated_word += random.choice(vowel if (start_with == 'vowel') else consonant)
    previous_letter = start_with
    for current_letter in range(1, length):
        generated_word += random.choice(consonant if (previous_letter == 'vowel') else vowel)
        previous_letter = 'consonant' if (previous_letter == 'vowel') else 'vowel'
    return generated_word

def generate_word_list(no_of_words, min_chars_in_word, max_chars_in_word):
    random.seed()
    words_list = []
    for x in range(no_of_words):
        words_list.append(generate_word(random.randint(min_chars_in_word, max_chars_in_word)))
    return words_list

# ===================================