from commands.create_command import *
from commands.keys import *
from model.index import *
 
class Table:
    def serialize(root_path,tablename):
        path = os.path.join(root_path,tablename[keys.NAME]+".json")
        with open(path, 'w') as json:
            Index.index(path,tablename)
            json.close()