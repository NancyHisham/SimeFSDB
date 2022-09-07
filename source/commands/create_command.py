import os, sys,json
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from commands.abstract_command import AbstractCommand
from commands.keys import *
from output.exceptions import *


class CreateCommand(AbstractCommand):
    def __init__(self , schema_path):
        self.schema_path = schema_path
        self.validate(self)  
    
    @staticmethod    
    def validate(self):
        parent_dir = os.getcwd()
        if (self.schema_path == None or not os.path.exists(os.path.join(parent_dir, self.schema_path))):
            raise SchemaNotFound("The schema path you entered is not found")

        try:  
            with open(self.schema_path, "r") as schema:
                self.data = json.load(schema)
        except:
            raise ErrorLoadingJsonFile("The json file could not be loaded")

        if not keys.DB_NAME in self.data:
            return DatabaseNameMissing("The database name is missing in your .json file")
    
    def excute(self):    
        self.__create_main_directory()

    def __create_main_directory(self):
        if(not os.path.exists(self.data[keys.DB_NAME])):
            os.mkdir(self.data[keys.DB_NAME]) 
        root_path = os.path.realpath(self.data[keys.DB_NAME])
        self.__create_table_folder(root_path)


    def __create_table_folder(self , root_path):
        if not keys.TABLES in self.data:
            return
        for tablename in self.data[keys.TABLES]:
            path = os.path.join(root_path, tablename[keys.NAME])
            os.makedirs(path, exist_ok = True)

