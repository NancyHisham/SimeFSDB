import unittest   # The test framework
import json
import os
from commands.create_command import CreateCommand


parent_dir = os. getcwd()
#print( "Current working dir : %s" % os.getcwd())
schema = "schema.json"
with open('schema.json','r') as fileData:
    data = json.load(fileData)

class TestAPICommand(unittest.TestCase):

    def test_wrong_schema_name(self):
        wrong_schema = "eskima.json"
        self.assertRaises(Exception, )
        wrong_schema = "schima.json"
        self.assertRaises(Exception, )
        wrong_schema = "skima.json"
        self.assertRaises(Exception, )

    def test_null_input(self):
        self.assertRaises(Exception, CreateCommand(None))
    
    def test_create_database(self):
        CreateCommand("schema.json")
        db_path = os.path.abspath(data[keys.DB_NAME])
        self.assertEqual(os.path.exists(db_path), True)

    def test_wrong_DB_Name(self):
        CreateCommand("schema.json")
        DB_Name = "Check"
        table = "FlightInfo"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)

    def test_create_multiple_times(self):
        DB_Name = "Check-in"
        db_path = os.path.join(parent_dir, DB_Name)
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            CreateCommand("schema.json")
            self.assertEqual(os.path.exists(db_path), True)

    def test_create_tables(self):
        CreateCommand("schema.json")
        for table in data[keys.TABLES]:
            table_path = os.path.join(parent_dir , data[keys.DB_NAME] , table[keys.NAME])
            self.assertEqual(os.path.exists(table_path), True)

    def test_wrong_table_name(self):
        CreateCommand("schema.json")
        DB_Name = "Check-in"
        table = "FlightDetails"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)

    
if __name__ == '__main__':
    args = parse_args()
    CreateCommand(args.schema)

    unittest.main()