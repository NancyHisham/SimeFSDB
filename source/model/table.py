from commands.create_command import *
from commands.keys import *
from model.index import *
from output.exceptions import *
import os

class Table:
    def __init__(self, root_path, tablename):
        self.root_path = root_path
        self.tablename = tablename
        self.path = os.path.join(self.root_path,self.tablename[keys.NAME])
        self.validate(self)
        
        
    def serialize(self):
        path = os.path.join(self.path + ".json")
        with open(path, 'w') as json:
            Index.index(path,self.tablename)
            json.close()
            
    @staticmethod
    def validate(self):
        if(not os.path.exists(self.root_path)):
            raise Exception()
        if(not os.path.exists(self.path)):
            raise Exception()