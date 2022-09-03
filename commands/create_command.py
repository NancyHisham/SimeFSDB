import json
import os
from commands.abstract_command import AbstractCommand
from keys import keys
from status_of_code import StatusOfCode

class CreateCommand(AbstractCommand):
    def __init__(self , schema_path):
        self.__validate_and_load_schema(schema_path)  
        
    def __validate_and_load_schema(self, schema_path):
        parent_dir = os.getcwd()
        if (schema_path == None or not os.path.exists(os.path.join(parent_dir, schema_path))):
            return StatusOfCode.SchemaNotFound

        try:  
            self.data = json.load(open(schema_path, "r"))
        except:
            return StatusOfCode.ErrorLoadingJsonFile

        if not keys.DB_NAME in self.data:
            return StatusOfCode.DatabaseNameIsMissing
        else:
            self.excute()
            return StatusOfCode.success
    
    def excute(self):    
        self.__create_main_directory()

    def __create_main_directory(self):
        if(not os.path.exists(self.data[keys.DB_NAME])):
            os.mkdir(self.data[keys.DB_NAME]) 
        root_path = os.path.realpath(self.data[keys.DB_NAME])
        CreateCommand.__create_table_folder(root_path,self.data)


    def __create_table_folder(root_path,data):
        if not keys.TABLES in data:
            return
        for tablename in data[keys.TABLES]:
                path = os.path.join(root_path, tablename[keys.NAME])
                os.makedirs(path, exist_ok = True)

