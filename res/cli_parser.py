import argparse

parser = argparse.ArgumentParser(description="Generate secure and easy to learn passphrases.")

parser.add_argument("--dict", 
                    required=True, 
                    type=str,
                    help="Specify which wordlist you"d like to use.")
parser.add_argument("--words", 
                    required=True, 
                    type=int,
                    help="Specify how many words you need to use in your passphrase.")
parser.add_argument("--sep", 
                    required=False, 
                    default="-",
                    type=str,
                    help="Which word separator should be used.")
parser.add_argument("--cap", 
                    required=False, 
                    default=False,
                    type=bool,
                    help=("Define whether used words should be capitalized "
                          "(first letter big). Put True or False"))
parser.add_argument("--number", 
                    required=False, 
                    default=False,
                    type=bool,
                    help=("Decide if you want to put one digit somewhere in the password. "
                          "Put True of False"))

args = parser.parse_args()
args_dict = vars(args)