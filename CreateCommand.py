import json
import os
# provides functions for creating, removing a directory (folder), fetching its contents, changing and identifying the current directory
from ICommand import ICommand
from Keys import Keys

class CreateCommand(ICommand):
    def execute(schema):
        with open('schema.json','r') as schema:
            """with ensures that the file is closed 
            when the block inside the with statement is exited."""
            data = json.load(schema)
            if(not os.path.exists(data[Keys.DB_Name])):
                os.mkdir(data[Keys.DB_Name])
            # else: # I commented both lines together using ctrl + /
            #     print("Check-in folder already exists")
            root_path = os.path.realpath(data[Keys.DB_Name])
            for tablename in data[Keys.tables]:
                path = os.path.join(root_path, tablename[Keys.name])
                if(not os.path.exists(path)):
                    os.mkdir(path)
#CreateCommand().execute()