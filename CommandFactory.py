
from CreateCommand import CreateCommand
from DeleteCommand import DeleteCommand
from GetCommand import GetCommand
from SetCommand import SetCommand


class CommandFactory:
    @staticmethod
    def build_command(args):
        command_type=args.command
        if command_type == "create":
            return CreateCommand(args.schema)
        elif command_type == "delete":
            return DeleteCommand(args.schema)
        elif command_type == "get":
            return GetCommand(args.schema)
        elif command_type == "set":
            return SetCommand(args.schema)
