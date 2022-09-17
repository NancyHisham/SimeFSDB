from commands.keys import *
import os, json
from model.table import *
from output.exceptions import *

class Database:
    
    def __init__(self):
        schema_data = self.__get_database_schema__()
        self.__validate(schema_data)
        self.DB_name = schema_data[keys.DB_NAME]
        Database.PATH = str(os.getcwd()).replace("model", "") # Path of the source directory
        self.__path__ = os.path.join(Database.PATH,self.DB_name) # the full path of the database
        self.tables = self.__create_tables(schema_data[keys.TABLES])
   
    @staticmethod
    def __validate(schema_data):
        if len(schema_data[keys.DB_NAME]) == 0 or schema_data[keys.DB_NAME].isspace():
            raise NoParameterError("Database name is not detected")

    def get_path(self):
        return self.__path__

    def create(self):
        self.__create_database()
        for table in self.tables:
            table.create()

    def __create_database(self):
        os.makedirs(self.__path__, exist_ok=True)
    
    def __get_database_schema__(self):
        with open(self.__path__, 'r') as schema_file:
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

