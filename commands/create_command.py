import json
import os
from keys import keys
from commands.abstract_command import ICommand

<<<<<<< Updated upstream
class CreateCommand(ICommand):
=======
class CreateCommand(ICommand): 
>>>>>>> Stashed changes

    def __init__(self):
        with open('schema.json','r') as schema:
            data = json.load(schema)
        self.excute(data)
        
    def excute(schema_path,data):
        if(not os.path.exists('schema.json')):
            return
        with open('schema.json','r'):
            if(not os.path.exists(data[keys.DB_Name])):
                os.mkdir(data[keys.DB_Name]) 
            root_path = os.path.realpath(data[keys.DB_Name])
            CreateCommand.__create_table_folder(root_path,data)

    def __create_table_folder(root_path,data):
        for tablename in data[keys.tables]:
                path = os.path.join(root_path, tablename[keys.name])
                if(not os.path.exists(path)):
                    os.mkdir(path)
            

            
