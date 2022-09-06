import unittest   # The test framework
import json
import os
from commands import set_command
from commands import createKey_command


class TestAPICommand(unittest.TestCase):

    def test_set(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_set"
        parameters = ["PlaneId", "AirLineName", "From", "To", "DepartureTime", "ArrivalTime"]
        values = ["123", "egyptAir", "alex", "oslo", "5AM", "2PM"]
        res = {"PlaneId":"123", "AirLineName":"egyptAir", "From":"alex", "To":"oslo", "DepartureTime":"5AM", "ArrivalTime":"2PM"}
        createKey_command.createKey(database, table, primary_key).execute()
        set_command.setCommand(database, table, primary_key, parameters, values).execute()
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        with open(path) as file:
            self.assertEqual(json.load(file), res)
            
            
    def test_invalid_types(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_invalid_types"
        parameters = ["PlaneId", "AirLineName", "From", "To", "DepartureTime", "ArrivalTime"]
        values = ["123", "egyptAir", "alex", "oslo", "5AM", "2PM"]
        res = {"PlaneId":"", "AirLineName":"", "From":"", "To":"", "DepartureTime":"", "ArrivalTime":""}
        createKey_command.createKey(database, table, primary_key).execute()
        try:
            set_command.setCommand(database, table, primary_key, "13213", values).execute()
        except Exception:
            pass
        
        try:
            set_command.setCommand(database, table, primary_key, parameters, "adsfads").execute()
        except Exception:
            pass
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        with open(path) as file:
            self.assertEqual(json.load(file), res)
          
    def test_null_input(self):
        try:
            set_command.setCommand(None , None, None, None, None).execute()
        except Exception:
            pass
        
        try:
            set_command.setCommand("" , table, "", parameters, "").execute()
        except Exception:
            pass
        
        try:
            set_command.setCommand(None , 312, None, None, 32).execute()
        except Exception:
            pass
        
    def test_parameters_and_values_not_same_len(self):
        database = "Check-in"
        table = "FlightInfo"
        primary_key = "test_notSameLen"
        parameters = ["PlaneId", "AirLineName", "From", "To", "DepartureTime", "ArrivalTime"]
        values = ["123", "egyptAir", "alex"]
        createKey_command.createKey(database, table, primary_key).execute()
        path = os.getcwd() + "\\" + database + "\\" + table + "\\" + primary_key + ".json"
        try:
            set_command.setCommand(database, table, primary_key, parameters, values).execute()
        except Exception:
            pass

    def test_wrong_DB_Name(self):
        database = "Check"
        table = "FlightInfo"
        primary_key = "test_wrong_DB_Name"
        parameters = ["PlaneId", "AirLineName", "From"]
        values = ["123", "egyptAir", "alex"]
        try:
            createKey_command.createKey(database, table, primary_key).execute()
        except Exception:
            pass
        
        try:
            set_command.setCommand(database, table, primary_key, parameters, values).execute()
        except Exception:
            pass

    def test_set_multiple_times(self):
        database = "Check-in"
        table = "FlightSeats"
        parameters = ["ReservationId"]
        values = ["123523423"]
        path = os.getcwd() + "\\" + database + "\\" + table
        for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
            createKey_command.createKey(database, table, i).execute()
            set_command.setCommand(database, table, i, parameters, values).execute()
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
        try:
            set_command.setValues(DB_Name, table, primary_key, parameters, values)
        except Exception:
            pass
    
if __name__ == '__main__':
    unittest.main()