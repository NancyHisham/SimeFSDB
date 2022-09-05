       
    # def test_null_input(self):
    #     self.assertEqual(False, createKey_command.createKey(None , None, None))

    # def test_wrong_DB_Name(self):
    #     DB_Name = "Check"
    #     table = "FlightInfo"
    #     self.assertEqual(False, createKey_command.createKey(DB_Name , table, "testWrongDB"))

    # def test_createKey_multiple_times(self):
    #     database = "Check-in"
    #     table = "FlightSeats"
    #     path = os.getcwd() + "\\" + database + "\\" + table
    #     for i in range(3): # this is an arbitratry number so that we can call the function more than one time 
    #         createKey_command.createKey(database , table, i)
    #         self.assertEqual(os.path.exists(path + "\\" + str(i) + ".json"), True)

    # def test_wrong_table_name(self):
    #     DB_Name = "Check-in"
    #     table = "FlightDetails"
    #     self.assertEqual(False, createKey_command.createKey(DB_Name , table, "testWrongTable"))
