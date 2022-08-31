from ParseInput import parse_args
from CommandFactory import CommandFactory
import os
import sys
os.path.join(os.getcwd(),"commands")
if __name__ == "__main__":
   #print("Enter your command: ")
   args = parse_args()
   command =CommandFactory().build_command(args)

