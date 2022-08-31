from ParseInput import parse_args
from CommandFactory import CommandFactory

if __name__ == "__main__":
   args = parse_args()
   args.command=input("Enter command: ")
   CommandFactory().build_command(args.command)



