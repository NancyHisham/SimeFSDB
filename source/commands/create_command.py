import os, sys,json
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from commands.abstract_command import AbstractCommand
from commands.keys import *
from output.exceptions import *
from model.table_matadata import *
from commands.keys import * 
 
class CreateCommand(AbstractCommand):

    def __init__(self , schema_path):
        self.data = CreateCommand.__validate_and_get_schema(schema_path)  

    @staticmethod
    def __validate_and_get_schema(schema_path):
        if (schema_path is None or schema_path == "" or schema_path == " "):
            raise  NoParameterError("The schema path was not entered")
        new_schema_path = os.path.join(keys.SCHEMA , schema_path) 
        if(not os.path.exists(new_schema_path)):
            raise SchemaNotFound("The schema path you entered is not found")
        return (CreateCommand.__load_data(new_schema_path))

    @staticmethod
    def __load_data(new_schema_path):
        try:  
            with open(new_schema_path, "r") as schema:
                data =  json.load(schema)
        except:
            raise ErrorLoadingJsonFile("The json file could not be loaded")

        if not keys.DB_NAME in data:
            raise DatabaseNameMissing("The database name is missing in your .json file")
        return data

    def excute(self):    
        self.__create_main_directory()
        root_path = os.path.realpath(self.data[keys.DB_NAME])
        self.__create_table_folders(root_path)

    def __create_main_directory(self):
        if(not os.path.exists(self.data[keys.DB_NAME])):
            os.mkdir(self.data[keys.DB_NAME]) 
        

    def __create_table_folders(self , root_path):
        if not keys.TABLES in self.data:
            return
        for tablename in self.data[keys.TABLES]:
            path = os.path.join(root_path, tablename[keys.NAME])
            os.makedirs(path, exist_ok = True)
            table_metadata = TableMetadata(tablename, path)
            table_metadata.serialize()


