import json
import os


def createKey(database, table, primary_key):
    if(not os.path.exists('schema.json')):
        return
    schema = json.load(open('schema.json','r'))
    for item in schema['Tables']:
        if item['name'] == table:
            columnsList = item["columns"]
            break
    json_columns = {}
    for parameter in columnsList:
        json_columns[parameter] = ""
    path = os.getcwd() + "\\" + database + "\\" + table
    if(not os.path.exists(path)):
        return "Error"
    path = path + "\\" + primary_key + ".json"
    
    with open( path , "w") as output:
        output.write(json.dumps(json_columns, indent=4))
    
        
createKey("Check-in", "FlightInfo", "abc")            
    