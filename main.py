from ParseInput import parse_args
from CommandFactory import CommandFactory

if __name__ == "__main__":
   args = parse_args()
   command =CommandFactory.build_command(args)

