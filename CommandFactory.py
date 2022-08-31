from CreateCommand import CreateCommand
from ParseInput import parse_args
args= parse_args()
class CommandFactory:
    @staticmethod
    def build_command(tt):
        command_type=tt
        if command_type == "create":
            return CreateCommand().excute()
#CommandFactory().build_command(args)