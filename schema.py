import json
import argparse
import sys
import os




def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")

    parser.add_argument(
        "-pk", 
        "--primary-key",
        type=str,
        help="Primary key is a unique key",
    )
    parser.add_argument(
        "-sc",
        "--schema",
        type=str,
        help="This is the database schema, it is a json object.",
    )
    return parser.parse_args()



def create(schema):
    with open('database.json','r') as database:
        data = json.load(database)
        if(os.path.exists(data[" database_name "])):
            return
        os.mkdir(data[" database_name "])
        root_path = os.path.realpath(data[" database_name "])
        for x in data[' Tables ']:
            path = os.path.join(root_path, x[' name '])
            os.mkdir(path)
         

args = parse_args()

create(args.schema)