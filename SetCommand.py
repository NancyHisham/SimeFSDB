import json
import os
# provides functions for creating, removing a directory (folder), fetching its contents, changing and identifying the current directory
from ICommand import ICommand
from Keys import Keys
class SetCommand(ICommand):
    def __init__(self,schema):
        self.schema=schema
    def excute(self):
        print("Set will be implemented later")