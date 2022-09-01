from CreateCommand import CreateCommand
from ParseInput import parse_args

class CommandFactory:
    args= parse_args()
    @staticmethod
    def create_command(args):
        command_type = args
        command_type = command_type.lower()
        if command_type == "create":
            CreateCommand().execute()
            
#CommandFactory().build_command(args)
