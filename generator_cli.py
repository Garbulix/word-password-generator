"""word-password-generator with CLI interface"""

import sys

import res.InterfaceBridge as controller
import res.cli_parser as CLI


# ===================================

if __name__ == '__main__':
    args = CLI.parser.parse_args()
    args_dict = vars(args)

    program = controller.InterfaceBridge()
    program.set_arguments(dictionary_name=args_dict["dict"])