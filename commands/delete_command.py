import json
import os
from abc import ABC

class deleteCommand(ABC):
    def __init__(self, database, table, primary_key):
        self.path = os.getcwd() + "\\" + str(database) + "\\" + str(table) + "\\" + str(primary_key) + ".json"
        self.validate(self, database, table, primary_key)
        
    def execute(self):
        os.remove(self.path)
        
    @staticmethod
    def validate(self, database, table, primary_key):
        if(database == None) or (table == None) or (primary_key == None):
            raise Exception()
        elif(not os.path.exists(self.path)):
            raise Exception()
        
        