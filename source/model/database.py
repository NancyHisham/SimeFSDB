from commands.keys import *
import os, json
from model.table import *
from output.exceptions import *

class Database:
    def __init__(self):
        self.schema_data = self.__get_database_schema__()
        self.__validate(self.schema_data)
        self.tables = self.__create_tables(self.schema_data[keys.TABLES])
        
   
    def __validate(self):
        if len(self.schema_data[keys.DB_NAME]) == 0 or self.schema_data[keys.DB_NAME].isspace():
            raise NoParameterError("Database name is missing")

    def create(self):
        self.__create_database()
        for table in self.tables:
            table.create()

    def __create_database(self):
        path = os.path.join(str(os.getcwd()).replace("model" , ""), self.schema_data[keys.DB_NAME]) # creates a database in the source folder
        os.makedirs(path, exist_ok=True)
    
    def __get_database_schema__(self):
        with open(self.schema_path, 'r') as schema_file:
            return json.load(schema_file)
    
    def __create_tables(self, schema_tables):
        self.tables = []
        for table_schema in schema_tables:
            self.tables.append(Table(table_schema[keys.NAME]))
        return table_schema

    
# schema_path = os.path.join(keys.SCHEMA , "schema.json") 


    # path = os.path.join(str(os.getcwd()).replace("model" , ""), self.schema_data[keys.DB_NAME]) # creates a database in the source folder
    # print("]]]]]]]]]]######################################")
    # print(path)
    # print("]]]]]]]]]]######################################")

