import json
import os


def createKey(database, table, primary_key):
    if(database == None) or (table == None) or (primary_key == None):
        return Exception()
    if(not os.path.exists('schema.json')):
        return Exception()
    with open('schema.json','r') as file:
        schema = json.load(file)
    columnsList = []
    for item in schema['Tables']:
        if item['name'] == table:
            columnsList = item["columns"]
            break
    json_columns = {}
    for parameter in columnsList:
        json_columns[parameter] = ""
    path = os.getcwd() + "\\" + database + "\\" + table
    if(not os.path.exists(path)):
        return Exception()  # or you call the create table method if the table is valid
    path = path + "\\" + str(primary_key) + ".json"
    
    with open( path , "w") as output:
        output.write(json.dumps(json_columns, indent=4))
    
        
createKey("Check-in", "FlightInfo", "abc")            
    