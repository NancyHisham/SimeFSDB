from commands.keys import *
import json
 
class Index:
    def index(path,tablename):
        indices = {"indices": []}
        for index in tablename[keys.IDX_KEY]:
            name_value = {"name": index, "values": []}
            indices["indices"].append(name_value)
        with open(path, 'w') as file:
            json.dump(indices, file) 