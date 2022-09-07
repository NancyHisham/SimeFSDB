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
        if self.args.command.lower() not in self.available_commands:
            raise WrongCommandError("Wrong command entered")

    def create_command(self):
        command_type = self.args.command.lower()
        if (command_type == "create"):
            return CreateCommand(self.args.schema)
        
        
