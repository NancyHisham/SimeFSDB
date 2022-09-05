import unittest   # The test framework
import json
import os
from commands import delete_command
from commands import createKey_command


class TestAPICommand(unittest.TestCase):

    def test_delete(self):
        database = "Check-in"
        table = "Reservations"
        primary_key = "test_delete"
        createKey_command.createKey(database , table, primary_key)
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        self.assertTrue(os.path.exists(path))
        delete_command.deleteCommand(database, table, primary_key)
        self.assertFalse(os.path.exists(path))
                    
                    
                
                
        
          
    def test_null_input(self):
        self.assertEqual(False, delete_command.deleteCommand(None, None, None))

    def test_wrong_DB_Name(self):
        DB_Name = "Check"
        table = "FlightInfo"
        primary_key = "test_wrong_DB_Name"
        self.assertEqual(False, delete_command.deleteCommand(DB_Name, table, primary_key))

    def test_createKey_multiple_times(self):
        database = "Check-in"
        table = "FlightSeats"
        path = os.getcwd() + "\\" + database + "\\" + table
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            createKey_command.createKey(database , table, i)
            self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), True)
        
        for i in range(3): 
            delete_command.deleteCommand(database , table, i)
            self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), False)

    def test_wrong_table_name(self):
        DB_Name = "Check-in"
        table = "FlightDetails"
        primary_key = "test_wrong_table_name"
        self.assertEqual(False, delete_command.deleteCommand(DB_Name, table, primary_key))

    
if __name__ == '__main__':
    unittest.main()