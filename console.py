#!/usr/bin/python3
""" Console Module """


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The console module class"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """This method has been edited to avoid executing
        the previous command when ENTER pressed
        """
        pass

    def postloop(self) -> None:
        """Method to handle ^D when entered to exit,
        so the terminal does not look messy."""
        print


if __name__ == "__main__":
    command = HBNBCommand()
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            command.onecmd(arg)
    else:
        HBNBCommand().cmdloop()
