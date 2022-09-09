import json, os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from commands.command_factory import CommandFactory
from output.output_message import *
from input_adaptors.parse_input import parse_args


if __name__ == "__main__":
   try:
      args = parse_args()
      command = CommandFactory(args).create_command()
      result = command.excute()
      output_obj = OutputMessage(command_name=args.command , result= result , exception = None)
   except Exception as e:
      output_obj = OutputMessage(command_name = args.command , result = None , exception = e)

   print(json.dumps(output_obj.__dict__))





#python main.py -command create -sc schema.json
#python main.py -command CREATE -sc schema.json