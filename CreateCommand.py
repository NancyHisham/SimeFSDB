import json
import os
# provides functions for creating, removing a directory (folder), fetching its contents, changing and identifying the current directory
from ICommand import ICommand
from Keys import Keys
class CreateCommand(ICommand):
    def __init__(self,schema):
        self.schema=schema
    def excute(self):
        file=open(self._schema,"r")
        data=json.load(file)
        parent_dir=os.getcwd() #get the current dir of the project
        database_name=data[Keys.DB_Name]
        path=os.path.join(parent_dir,database_name)
        os.makedirs(path)
        print("Directory '%s' created" %data[Keys.DB_Name])
        for table in data[Keys.tables]:
            table_path=os.path.join(path,table[Keys.name])
            os.makedirs(table_path, exist_ok=False)
            print("Directory '%s' created" %table[Keys.name])
        file.close()