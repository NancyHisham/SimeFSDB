import json
import os


def delete_command(database, table, primary_key):
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        return Exception()
    os.remove(path)
    return 0
    
    