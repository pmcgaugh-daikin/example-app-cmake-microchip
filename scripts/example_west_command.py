# Copyright (c) 2019 Foundries.io
# Copyright (c) 2022 Nordic Semiconductor ASA
# SPDX-License-Identifier: Apache-2.0

'''example_west_command.py

Example of a west extension in the example-application repository.'''

from west.commands import WestCommand  # your extension must subclass this
from west import log                   # use this for user output

class ExampleWestCommand(WestCommand):

    def __init__(self):
        """
        Initializes an instance of a class by calling the parent class's
        `super().__init__` and setting properties for the current class, including
        the name, help message, and description of the class.

        """
        super().__init__(
            'example-west-command',               # gets stored as self.name
            'an example west extension command',  # self.help
            # self.description:
            '''\
A multi-line description of example-west-command.

You can split this up into multiple paragraphs and they'll get
reflowed for you. You can also pass
formatter_class=argparse.RawDescriptionHelpFormatter when calling
parser_adder.add_parser() below if you want to keep your line
endings.''')

    def do_add_parser(self, parser_adder):
        # This is a bit of boilerplate, which allows you full control over the
        # type of argparse handling you want. The "parser_adder" argument is
        # the return value of an argparse.ArgumentParser.add_subparsers() call.
        """
        Adds a new parser to an existing argparse.ArgumentParser instance, allowing
        full control over the type of argparse handling. It adds various options
        using the standard argparse module API and returns the created parser.

        Args:
            parser_adder (`argparse.ArgumentParser`.): result of an
                `argparse.ArgumentParser.add_subparsers()` call, which provides
                full control over the type of argparse handling desired.
                
                		- `parser`: A `argparse.ArgumentParser` object, which is the
                return value of `argparse.ArgumentParser.add_subparsers()` call.
                		- `name`: The name of the parser, which is set to the function's
                name (`self.name`).
                		- `help`: The help message for the parser, which is set to the
                function's `help` variable.
                		- `description`: The description of the parser, which is set to
                the function's `description` variable.

        Returns:
            argparse.ArgumentParser: an instance of `argparse.Parser` class, which
            can be used to handle and validate command-line arguments for the given
            function or module.
            
            		- `parser`: A `argparse.ArgumentParser` instance representing the
            customized parser added with the function. This is the primary return
            value of the function and allows full control over the type of argparse
            handling desired.
            		- `name`: The name of the parser, which can be used to access or
            modify its properties and behavior.
            		- `help`: A string indicating a brief description of the parser's
            functionality, which can be displayed to the user when they run the
            program with the `-h` or `--help` option.
            		- `description`: A longer string describing the parser's functionality,
            which can be used to provide additional context for the user when they
            run the program with the `--explain` or `-e` option.
            
            	Overall, the `do_add_parser` function is a utility method that allows
            you to add customized arguments and subcommands to an existing argparse
            parser, providing a high degree of control over the resulting parser's
            behavior and output.

        """
        parser = parser_adder.add_parser(self.name,
                                         help=self.help,
                                         description=self.description)

        # Add some example options using the standard argparse module API.
        parser.add_argument('-o', '--optional', help='an optional argument')
        parser.add_argument('required', help='a required argument')

        return parser           # gets stored as self.parser

    def do_run(self, args, unknown_args):
        # This gets called when the user runs the command, e.g.:
        #
        #   $ west my-command-name -o FOO BAR
        #   --optional is FOO
        #   required is BAR
        """
        Is called when the user runs the command, and it logs information about
        the optional and required arguments passed to the function.

        Args:
            args (instance of WestArguments class.): command-line arguments passed
                to the function, including both required and optional arguments.
                
                		- `optional`: A string that represents the value passed as an
                optional parameter.
                		- `required`: A string that represents the value passed as a
                required parameter.
            unknown_args (`argparse.Parser`.): additional arguments passed to the
                `do_run()` function beyond those specified by the user.
                
                		- `optional`: This attribute contains the value of any optional
                arguments passed to the command.
                		- `required`: This attribute contains the value of any required
                arguments that were not provided in the input.

        """
        log.inf('--optional is', args.optional)
        log.inf('required is', args.required)
