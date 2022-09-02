<<<<<<< Updated upstream
import unittest   # The test framework
import json
=======
import unittest
import json
<<<<<<<< Updated upstream:test_create.py
>>>>>>> Stashed changes
import os
from keys import keys
from commands.create_command import CreateCommand
parent_dir = os. getcwd()
#print( "Current working dir : %s" % os.getcwd())
schema = "schema.json"
<<<<<<< Updated upstream
with open('schema.json','r') as fileData:
=======
with open('schema.json','r') as fileData: 
>>>>>>> Stashed changes
    data = json.load(fileData)

class TestCreateCommand(unittest.TestCase):

    def test_wrong_schema_name(self):
        wrong_schema = "eskima.json"
        self.assertRaises(Exception, CreateCommand.excute(wrong_schema,data))
        wrong_schema = "schima.json"
        self.assertRaises(Exception, CreateCommand.excute(wrong_schema,data))
        wrong_schema = "skima.json"
        self.assertRaises(Exception, CreateCommand.excute(wrong_schema,data))

    def test_null_input(self):
        self.assertRaises(Exception, CreateCommand.excute(None,data))

    def test_create_database(self):
        db_path = os.path.abspath(data[keys.DB_Name])
        self.assertEqual(os.path.exists(db_path), True)

    def test_wrong_DB_Name(self):
        DB_Name = "Check"
        table = "FlightInfo"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)

    def test_create_multiple_times(self):
        DB_Name = "Check-in"
        db_path = os.path.join(parent_dir, DB_Name)
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            CreateCommand().excute(data)
            self.assertEqual(os.path.exists(db_path), True)

    def test_create_tables(self):
        for table in data[keys().tables]:
            table_path = os.path.join(parent_dir , data[keys().DB_Name] , table[keys().name])
            self.assertEqual(os.path.exists(table_path), True)

    def test_wrong_table_name(self):
        DB_Name = "Check-in"
        table = "FlightDetails"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)
if __name__ == '__main__':
    CreateCommand().excute(data)
<<<<<<< Updated upstream
=======
========
import argparse
import sys
import os

class databaseTest(unittest.TestCase): 
    
    def test1(self):
        with open("database.json", 'r') as database:
            data = json.load(database)
            root_path = os.path.realpath(data["database_name"])
            if(not os.path.exists(root_path)):
                self.assertEqual(False)
            for x in data['Tables']:
                path = os.path.join(root_path, x['name'])
                if(not os.path.exists(path)):
                    self.assertTrue(False)
        self.assertTrue(True)
        
     
if __name__ == '__main__':
>>>>>>>> Stashed changes:test.py
>>>>>>> Stashed changes
    unittest.main()