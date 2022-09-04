import json
import os
import createKey_command


def set_command(database, table, primary_key, parameter, value):
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        createKey_command.createKey(database, table, primary_key)
    data = json.load(open(path, 'r'))
    parameter = list(parameter)
    value = list(value)
    for i in range(len(parameter)):
        if not (parameter[i] in data):
            return Exception()
        data[parameter[i]] = value[i]
    with open( path , "w") as output:
        output.write(json.dumps(data, indent=4))
    return 0
    
    

set_command("Check-in", "FlightInfo", "abc", ["PlaneId", "AirLineName", "From"], ["124", "egyptair", "alex"])