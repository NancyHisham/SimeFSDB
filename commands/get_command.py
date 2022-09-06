import json
import os
from abc import ABC

class getCommand(ABC):
    def __init__(self, database, table, primary_key, parameters=[]):
        self.validate(self, database, table, primary_key, parameters)
        path = os.getcwd() + "\\" + str(database) + "\\" + str(table) + "\\" + str(primary_key) + ".json"
        with open(path, 'r') as file:
            self.data = json.load(file)
        self.parameters = parameters
        self.checkParameters(self)

    def execute(self):
        if(self.parameters == []):
            return self.data
        res = {}
        for i in range(len(self.parameters)):
            res[self.parameters[i]] = self.data[self.parameters[i]]
        return res
    
    @staticmethod
    def validate(self, database, table, primary_key, parameters):
        path = os.getcwd() + "\\" + str(database) + "\\" + str(table) + "\\" + str(primary_key) + ".json"
        if(database == None) or (table == None) or (primary_key == None):
            raise Exception()
        elif(not os.path.exists(path)):
            raise Exception()
        elif(type(parameters) != list):
            raise Exception()
            
    @staticmethod
    def checkParameters(self):
        if (self.parameters != []):
            for i in range(len(self.parameters)):
                if not (self.parameters[i] in self.data):
                    raise Exception()
                    break
            