import json
import os
from commands import createKey_command


def setValues(database, table, primary_key, parameters, values):
    if(database == None) or (table == None) or (primary_key == None) or (parameters == None) or (values == None):
        return False
    if(len(parameters) != len(values)):
        return False
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        if not createKey_command.createKey(database, table, primary_key):
            return False
    with open(path, 'r') as file:
        data = json.load(file)
    parameters = list(parameters)
    values = list(values)
    for i in range(len(parameters)):
        if not (parameters[i] in data):
            return False
        data[parameters[i]] = values[i]
    with open( path , "w") as output:
        output.write(json.dumps(data, indent=4))
    return True