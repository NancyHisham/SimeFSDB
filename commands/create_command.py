import json
import os
from commands.abstract_command import AbstractCommand
from keys import keys

class CreateCommand(AbstractCommand):

    def __init__(self):
        with open('schema.json','r') as schema:
            data = json.load(schema)
        self.excute(data)
        
    def excute(schema_path,data):
        if(not os.path.exists('schema.json')):
            return
        with open('schema.json','r'):
            if(not os.path.exists(data[keys.DB_NAME])):
                os.mkdir(data[keys.DB_NAME]) 
            root_path = os.path.realpath(data[keys.DB_NAME])
            CreateCommand.__create_table_folder(root_path,data)

    def __create_table_folder(root_path,data):
        for tablename in data[keys.TABLES]:
                path = os.path.join(root_path, tablename[keys.NAME])
                if(not os.path.exists(path)):
                    os.mkdir(path)
            

            
