import json
import os


def get_command(database, table, primary_key, parameter):
    path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
    if(not os.path.exists(path)):
        return "Error, does't exist"
    data = json.load(open(path, 'r'))
    if not (parameter in data):
        return "Error, key doesn't exist"
    return data[parameter]
    
    

print(get_command("Check-in", "FlightInfo", "abc", "PlaneId"))