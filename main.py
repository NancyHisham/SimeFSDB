from parse_input import parse_args
from commands.command_factory import CommandFactory

if __name__ == "__main__":
   args = parse_args()
   CommandFactory.create_command(args)