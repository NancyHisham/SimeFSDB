import os, sys,json
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from commands.abstract_command import AbstractCommand
from commands.keys import *
from output.exceptions import *


class CreateCommand(AbstractCommand):
    def __init__(self , schema_path):
        self.schema_path = schema_path
        self.validate()  
        
    def validate(self):
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        if (self.schema_path is None or self.schema_path == "" or self.schema_path == " "):
            raise  NoParameterError("The schema path was not entered")
        new_path =os.path.join(parent_dir.replace("commands",'').replace("source", ''),'tests', self.schema_path)
        if(not os.path.exists(new_path)):
            raise SchemaNotFound("The schema path you entered is not found")

        try:  
            with open(new_path, "r") as schema:
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

