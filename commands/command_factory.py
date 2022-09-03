from commands.create_command import CreateCommand

class CommandFactory:
    def create_command(args):
        command_type = args.command.lower()
        if (command_type == "create"):
            return CreateCommand(args.schema)
        
