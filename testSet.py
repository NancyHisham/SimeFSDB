import unittest   # The test framework
import json
import os
from commands import set_command


class TestAPICommand(unittest.TestCase):

    def test_set(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_set"
        parameters = ["PlaneId", "AirLineName", "From", "To", "DepartureTime", "ArrivalTime"]
        values = ["123", "egyptAir", "alex", "oslo", "5AM", "2PM"]
        res = {"PlaneId":"123", "AirLineName":"egyptAir", "From":"alex", "To":"oslo", "DepartureTime":"5AM", "ArrivalTime":"2PM"}
        set_command.setValues(database, table, primary_key, parameters, values)
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        with open(path) as file:
            self.assertEqual(json.load(file), res)
          
    def test_null_input(self):
        self.assertEqual(False, set_command.setValues(None , None, None, None, None))
        
    def test_parameters_and_values_not_same_len(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_notSameLen"
        parameters = ["PlaneId", "AirLineName", "From", "To", "DepartureTime", "ArrivalTime"]
        values = ["123", "egyptAir", "alex"]
        self.assertEqual(False, set_command.setValues(database, table, primary_key, parameters, values))
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        self.assertFalse(os.path.exists(path))

    def test_wrong_DB_Name(self):
        DB_Name = "Check"
        table = "FlightInfo"
        primary_key = "test_wrong_DB_Name"
        parameters = ["PlaneId", "AirLineName", "From"]
        values = ["123", "egyptAir", "alex"]
        self.assertEqual(False, set_command.setValues(DB_Name, table, primary_key, parameters, values))

    def test_create_multiple_times(self):
        database = "Check-in"
        table = "FlightSeats"
        parameters = ["ReservationId"]
        values = ["123523423"]
        path = os.getcwd() + "\\" + database + "\\" + table
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            set_command.setValues(database, table, str(i), parameters, values)
            self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), True)
            with open((path + "\\" + str(i) + ".json"), 'r') as file:
                json_file = json.load(file)
                i = 0
                for parameter in parameters:
                    self.assertEqual(json_file[parameter], values[i])
                    i += 1

    def test_wrong_table_name(self):
        DB_Name = "Check-in"
        table = "FlightDetails"
        primary_key = "test_wrong_table_name"
        parameters = ["ReservationId"]
        values = ["123523423"]
        self.assertEqual(False, set_command.setValues(DB_Name, table, primary_key, parameters, values))

    
if __name__ == '__main__':
    unittest.main()