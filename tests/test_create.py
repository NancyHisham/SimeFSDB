import unittest   # The test framework
import json , sys , os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(root_dir)
from source.output.exceptions import * 
from source.commands.keys import keys
from source.commands.create_command import CreateCommand
from source.input_adaptors.parse_input import parse_args
schema_path = os.path.join(root_dir, "tests" , "schema.json")

parent_dir = os. getcwd()

with open(schema_path,'r') as fileData:
    data = json.load(fileData)

class TestCreateCommand(unittest.TestCase):

    def test_wrong_schema_name(self):
        self.assertRaises(Exception, CreateCommand , None)
        self.assertRaises(Exception, CreateCommand , "schima.json")
        self.assertRaises(Exception, CreateCommand , "eskima.json")
        self.assertRaises(Exception, CreateCommand , "skima.json")

    def test_create_database(self):
        CreateCommand(schema_path).excute()
        db_path = os.path.abspath(data[keys.DB_NAME])
        self.assertEqual(os.path.exists(db_path), True)
    
    def test_wrong_DB_Name(self):
        CreateCommand(schema_path).excute()
        DB_Name = "Check"
        table = "FlightInfo"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)

    def test_create_multiple_times(self):
        DB_Name = "Check-in"
        db_path = os.path.join(parent_dir, DB_Name)
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            CreateCommand(schema_path).excute()
            self.assertEqual(os.path.exists(db_path), True)

    def test_create_tables(self):
        CreateCommand(schema_path).excute()
        for table in data[keys.TABLES]:
            table_path = os.path.join(parent_dir , data[keys.DB_NAME] , table[keys.NAME])
            self.assertEqual(os.path.exists(table_path), True)
    
    def test_wrong_table_name(self):
        CreateCommand(schema_path).excute()
        DB_Name = "Check-in"
        table = "FlightDetails"
        t_path = os.path.join(parent_dir, DB_Name, table)
        self.assertEqual(os.path.exists(t_path), False)

if __name__ == '__main__':
    unittest.main()