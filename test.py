import unittest   # The test framework
import json
import os, sys
from Keys import Keys
from CreateCommand import CreateCommand
parent_dir = os. getcwd()
#print( "Current working dir : %s" % os.getcwd())
schema = "schema.json"
with open('schema.json','r') as fileData:
    data = json.load(fileData)

class TestCreateCommand(unittest.TestCase):
    
    def test_wrong_schema_name(self):
        wrong_schema = "eskima.json"
        self.assertRaises(Exception, CreateCommand.execute(wrong_schema))
        wrong_schema = "schima.json"
        self.assertRaises(Exception, CreateCommand.execute(wrong_schema))
        wrong_schema = "skima.json"
        self.assertRaises(Exception, CreateCommand.execute(wrong_schema))

    def test_null_input(self):
        self.assertRaises(Exception, CreateCommand.execute(None))

    def test_create_database(self):
        db_path = os.path.abspath(data[Keys.DB_Name])
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
            CreateCommand().execute()
            self.assertEqual(os.path.exists(db_path), True)

    def test_create_tables(self):
        for table in data[Keys().tables]:
            table_path = os.path.join(parent_dir , data[Keys().DB_Name] , table[Keys().name])
            self.assertEqual(os.path.exists(table_path), True)
    
    def test_wrong_table_name(self):
        DB_Name = "Check-in"
        table = "FlightDetails"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)
if __name__ == '__main__':
    CreateCommand().execute()
    unittest.main()