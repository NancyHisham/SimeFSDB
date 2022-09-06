import unittest   # The test framework
import json
import os
from commands import createKey_command


class TestAPICommand(unittest.TestCase):

    def test_createKey(self):
        database = "Check-in"
        table = "Reservations"
        primary_key = "test_createKey"
        createKey_command.createKey(database , table, primary_key)
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        self.assertTrue(os.path.exists(path))
        
        with open('schema.json','r') as file:
            schema = json.load(file)
        columnsList = []
        for item in schema['Tables']:
            if item['name'] == table:
                columnsList = item["columns"]
                break
        with open(path) as file:
            file = json.load(file)
            i = 0
            for key in file:
                self.assertEqual(key, columnsList[i])
                i += 1
  
    def test_null_input(self):
        self.assertEqual(False, createKey_command.createKey(None , None, None))

    def test_wrong_DB_Name(self):
        DB_Name = "Check"
        table = "FlightInfo"
        self.assertEqual(False, createKey_command.createKey(DB_Name , table, "testWrongDB"))

    def test_createKey_multiple_times(self):
        database = "Check-in"
        table = "FlightSeats"
        path = os.getcwd() + "\\" + database + "\\" + table
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            createKey_command.createKey(database , table, i)
            self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), True)

    def test_wrong_table_name(self):
        DB_Name = "Check-in"
        table = "FlightDetails"
        self.assertEqual(False, createKey_command.createKey(DB_Name , table, "testWrongTable"))

    
if __name__ == '__main__':
    unittest.main()