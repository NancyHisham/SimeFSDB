import unittest   # The test framework
import json
import os
from commands import set_command
from commands import get_command


class TestAPICommand(unittest.TestCase):

    def test_get(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_get"
        parameters = ["PlaneId", "AirLineName", "From", "To"]
        values = ["123", "egyptAir", "alex", "oslo"]
        res = {"PlaneId":"123", "AirLineName":"egyptAir", "From":"alex", "To":"oslo"}
        set_command.setValues(database, table, primary_key, parameters, values)
        self.assertEqual(res, get_command.getCommand(database, table, primary_key, parameters))
          
    def test_null_input(self):
        self.assertEqual(False, get_command.getCommand(None, None, None, None))
        
    def test_parameters_not_given(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_parameters_not_given"
        parameters = ["PlaneId", "AirLineName", "From", "To"]
        values = ["123", "egyptAir", "alex", "oslo"]
        res = {"PlaneId":"123", "AirLineName":"egyptAir", "From":"alex", "To":"oslo", "DepartureTime": "", "ArrivalTime": ""}
        set_command.setValues(database, table, primary_key, parameters, values)
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        self.assertEqual(res, get_command.getCommand(database, table, primary_key))

    def test_wrong_DB_Name(self):
        DB_Name = "Check"
        table = "FlightInfo"
        primary_key = "test_wrong_DB_Name"
        parameters = ["PlaneId", "AirLineName", "From"]
        self.assertEqual(False, get_command.getCommand(DB_Name, table, primary_key, parameters))

    def test_create_multiple_times(self):
        database = "Check-in"
        table = "FlightSeats"
        parameters = ["ReservationId"]
        values = ["123523423"]
        res = {"ReservationId" : "123523423"}
        path = os.getcwd() + "\\" + database + "\\" + table
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            set_command.setValues(database, table, str(i), parameters, values)
            self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), True)
        for i in range(3):
            self.assertEqual(res, get_command.getCommand(database, table, str(i)))

    def test_wrong_table_name(self):
        database = "Check-in"
        table = "FlightDetails"
        primary_key = "test_wrong_table_name"
        parameters = ["ReservationId"]
        values = ["123523423"]
        self.assertEqual(False, get_command.getCommand(database, table, primary_key))

    
if __name__ == '__main__':
    unittest.main()