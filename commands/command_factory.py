from commands.create_command import CreateCommand
from parse_input import parse_args

<<<<<<< Updated upstream
class CommandFactory:
=======
class CommandFactory: 
>>>>>>> Stashed changes
    args = parse_args()
    
    def build_command(args):
        command = args.command
        if (command == "create"):
            return CreateCommand()
        
#CommandFactory.build_command(command_type)

