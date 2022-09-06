import json
import os
from abc import ABC

class setCommand(ABC):
    def __init__(self, database, table, primary_key, parameters, values):
        self.path = os.getcwd() + "\\" + str(database) + "\\" + str(table) + "\\" + str(primary_key) + ".json"
        self.validate(self, database, table, primary_key, parameters, values)
        with open(self.path, 'r') as file:
            self.data = json.load(file)
        self.parameters = parameters
        self.checkParameters(self)
        self.values = values

    def execute(self):
        for i in range(len(self.parameters)):
            self.data[self.parameters[i]] = self.values[i]
        with open(self.path , "w") as output:
            output.write(json.dumps(self.data, indent=4))

    
    @staticmethod
    def validate(self, database, table, primary_key, parameters, values):
        if(database == None) or (table == None) or (primary_key == None):
            raise Exception()
        elif(not os.path.exists(self.path)):
            raise Exception()
        elif(type(parameters) != list):
            raise Exception()
        elif(type(values) != list):
            raise Exception()
        elif(len(parameters) != len(values)):
            raise Exception("abc")
            
    @staticmethod
    def checkParameters(self):
        if (self.parameters != []):
            for i in range(len(self.parameters)):
                if not (self.parameters[i] in self.data):
                    raise Exception()
                    break
    