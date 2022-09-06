import json
import os
from abc import ABC

class createKey(ABC):
    def __init__(self, database, table, primary_key):
        self.validate(self, str(database), str(table), str(primary_key))
        self.path = os.getcwd() + "\\" + str(database) + "\\" + str(table) + "\\" + str(primary_key) + ".json"
        self.table = table
        
    def execute(self):
        columnsList = []
        for item in self.schema['Tables']:
            if item['name'] == self.table:
                columnsList = item["columns"]
                break
        json_columns = {}
        for parameter in columnsList:
            json_columns[parameter] = ""
        
        with open(self.path , "w") as output:
            output.write(json.dumps(json_columns, indent=4))
    
    @staticmethod
    def validate(self, database, table, primary_key):
        if(database == None) or (table == None) or (primary_key == None):
            raise Exception()
        elif(database == "") or (table == "") or (primary_key == ""):
            raise Exception()
        elif(database.isspace()) or (table.isspace()) or (primary_key.isspace()):
            raise Exception()
        elif(not os.path.exists(os.path.join(os.getcwd(), str(database), str(table)))):
            raise Exception()
        elif(not os.path.exists('schema.json')):
            raise Exception()
        else:
            with open('schema.json','r') as file:
                self.schema = json.load(file)
            if self.schema["database_name"] != database:
                raise Exception()