"""word-password-generator with CLI interface"""
# TODO translate

import sys

import res.InterfaceBridge as controller
import res.cli_parser as CLI


# ===================================

if __name__ == '__main__':
    try:
        parsed_args = CLI.parser.parse_args()
        args = vars(parsed_args) # convertion to dict
        program = controller.InterfaceBridge()
        
        passwd = program.get_another_password(dictionary_name=args["dict"],
                                            word_count=args["words"],
                                            used_separator=args["sep"],
                                            if_capitalize=args["capitalize"],
                                            if_insert_number=args["add_number"])

        print(passwd)
    except:
        print("Some error occured :<")