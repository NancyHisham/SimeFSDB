import json
import os


def getCommand(database, table, primary_key, parameters=None):
    database = str(database)
    table = str
    
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        return False
    with open(path, 'r') as file:
        data = json.load(file)
    if(parameters == None):
        return data
    res = {}
    for i in range(len(parameters)):
        if not (parameters[i] in data):
            return False
        res[parameters[i]] = data[parameters[i]]
    return res