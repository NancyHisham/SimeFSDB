from commands.create_command import CreateCommand
from parse_input import parse_args

class CommandFactory:
    def create_command(args):
        cmnd = args.command.lower()
        if (cmnd == "create"):
            return CreateCommand()
        
#CommandFactory.create_command(command_type)
