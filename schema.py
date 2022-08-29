import json
import argparse
import sys
import os




def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(
<<<<<<< Updated upstream
=======
        "-cmd",
        "--command",
        type=str,
        help= "Command : Create , Get , Set , Delete",
    )
    parser.add_argument(
>>>>>>> Stashed changes
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
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="The Database name",
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="The Table name",
    )
    parser.add_argument(
        "-v",
        "--value",
        type=str,
        help="The Value to add",
    )
    return parser.parse_args()



def create(schema):
    with open('database.json','r') as database:
        data = json.load(database)
        if(os.path.exists(data["database_name"])):
            print("Already Exist")
            return
        os.mkdir(data["database_name"])
        root_path = os.path.realpath(data["database_name"])
        for x in data['Tables']:
            path = os.path.join(root_path, x['name'])
            os.mkdir(path)
         

cmd = input("Enter create : ")
class CommandFactory:
    args = parse_args()
    if (cmd == "create") :
        create(args.schema)