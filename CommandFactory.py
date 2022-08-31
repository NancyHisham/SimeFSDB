from CreateCommand import CreateCommand
from ParseInput import parse_args

class CommandFactory:
    args= parse_args()
    @staticmethod
    def create_command(args):
        command_type=args
        if command_type == "create":
            return CreateCommand().excute()
#CommandFactory().build_command(args)