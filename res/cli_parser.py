"""Parsing arguments from commandline interface"""

import argparse

# TODO translate, create class that converts passed argv

parser = argparse.ArgumentParser(description="Generate secure and easy to learn passphrases.")

def str_to_bool(value):
    if value.lower() in {'false', 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 't', '1', 'yes', 'y'}:
        return True
    else: 
        raise Exception(f'{value} is not a valid boolean value') from ValueError

parser.add_argument("-d", "--dict", 
                    required=True, 
                    type=str,
                    help="Specify which wordlist you'd like to use. "
                         "Currently available: " 
                         "polish, "
                         "english, "
                         "english-unique (unique three-character prefixes).")
parser.add_argument("-w", "--words", 
                    required=True, 
                    type=int,
                    help="Specify how many words you need to use in your passphrase.")
parser.add_argument("-s", "--sep", 
                    required=False, 
                    default="-",
                    type=str,
                    help="Which word separator should be used. "
                         "Dash is default separator.")
parser.add_argument("-c", "--capitalize", 
                    required=False, 
                    default=False,
                    type=str_to_bool, 
                    nargs='?', 
                    const=True,
                    help=("Use if you want to capitalize all words. "
                          "Not-capitalizing is default action."))
parser.add_argument("-n", "--add-number", 
                    required=False, 
                    default=False,
                    type=str_to_bool, 
                    nargs='?', 
                    const=True,
                    help=("Use if you want to put a number somewhere in passphrase. "
                          "Adding number isn't default action."))