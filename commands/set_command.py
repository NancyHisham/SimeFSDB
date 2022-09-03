import json
import os
import createKey_command


def set_command(database, table, primary_key, parameter, value):
    path = os.getcwd() + "\ " + database + "\ " + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        createKey_command.createKey(database, table, primary_key)
    data = json.load(open(path, 'r'))
    if not (parameter in data):
        return "Error, key doesn't exist"
    data[parameter] = value
    with open( path , "w") as output:
        output.write(json.dumps(data, indent=4))
    
    

set_command("Check-in", "FlightInfo", "abc", "PlaneId", "124")
set_command("Check-in", "FlightInfo", "abc", "AirLineName", "egyptair")
set_command("Check-in", "FlightInfo", "abc", "From", "alex")