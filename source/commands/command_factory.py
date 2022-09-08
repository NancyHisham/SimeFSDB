import os,sys
sys.path.append(os.path.join(os.getcwd(), "commands"))

from commands.create_command import CreateCommand
from source.output.exceptions import *
import os,sys

class CommandFactory:
    def __init__(self, args):
        self.args = args
        self.available_commands = {"create", "set", "get", "delete"}
        self.validate(self)

    @staticmethod
    def validate(self):
        command_type = self.args.command.lower() if self.args.command is not None else None
        if command_type is None:
            raise NoCommandEntered("A command must be entered")
        elif command_type not in self.available_commands:
            raise WrongCommandError("Wrong command entered")

    def create_command(self):
        command_type = self.args.command.lower()
        if (command_type == "create"):
            return CreateCommand(self.args.schema)
        
        
