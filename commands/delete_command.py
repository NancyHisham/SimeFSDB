import json
import os


def deleteCommand(database, table, primary_key):
    if(database == None) or (table == None) or (primary_key == None):
        return False
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + str(primary_key) + ".json"
    if(not os.path.exists(path)):
        return False
    os.remove(path)
    return True
    
    