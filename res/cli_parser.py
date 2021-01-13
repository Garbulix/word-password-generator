import argparse

parser = argparse.ArgumentParser(description="Generate secure and easy to learn passphrases.")

def str_to_bool(value):
    if value.lower() in {'false', 'False' 'f', '0', 'no', 'n'}:
        return False
    elif value.lower() in {'true', 'False' 't', '1', 'yes', 'y'}:
        return True
    raise ValueError(f'{value} is not a valid boolean value')

# TODO nargs, const

parser.add_argument("--dict", 
                    required=True, 
                    type=str,
                    help="Specify which wordlist you'd like to use. "
                         "Currently available: " 
                         "polish, "
                         "english, "
                         "english-unique (unique three-character prefixes)")
parser.add_argument("--words", 
                    required=True, 
                    type=int,
                    help="Specify how many words you need to use in your passphrase.")
parser.add_argument("--sep", 
                    required=False, 
                    default="-",
                    type=str,
                    help="Which word separator should be used.")
parser.add_argument("--capitalize", 
                    required=False, 
                    default=False,
                    type=str_to_bool, 
                    nargs='?', 
                    const=True,
                    help=("Use if you want to capitalize all words."))
parser.add_argument("--add-number", 
                    required=False, 
                    default=False,
                    type=str_to_bool, 
                    nargs='?', 
                    const=True,
                    help=("Use if you want to put a number somewhere in passphrase."))