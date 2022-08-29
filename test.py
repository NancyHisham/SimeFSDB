import unittest
import json
import argparse
import sys
import os

class databaseTest(unittest.TestCase): 
    
    def test1(self):
        with open("database.json", 'r') as database:
            data = json.load(database)
            root_path = os.path.realpath(data["database_name"])
            if(not os.path.exists(root_path)):
                self.assertTrue(False)
            for x in data['Tables']:
                path = os.path.join(root_path, x['name'])
                if(not os.path.exists(path)):
                    self.assertTrue(False)
        self.assertTrue(True)
        
     
if __name__ == '__main__':
    unittest.main()
