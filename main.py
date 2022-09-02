from parse_input import parse_args
from commands.command_factory import CommandFactory

if __name__ == "__main__": 
   args = parse_args()
   args.command = input("Enter create: ")
   args.command = args.command.lower()
   CommandFactory.build_command(args)