"""word-password-generator with CLI interface"""

import sys

import res.InterfaceBridge as controller
import res.cli_parser as CLI


# ===================================

if __name__ == '__main__':
    parsed_args = CLI.parser.parse_args()
    args = vars(parsed_args) # convertion to dict
    program = controller.InterfaceBridge()
    
    program.set_arguments(dictionary_name=args["dict"],
                          word_count=args["words"],
                          separator=args["sep"],
                          if_capitalize=args["capitalize"],
                          if_insert_number=args["add_number"])

    print(program.get_next_password())