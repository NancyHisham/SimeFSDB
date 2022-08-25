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



def creat(schema):
    xs = [None] * 3
    i=0
    with open('database.py','r') as file:
        say1 = 'database_name'
        say2 = 'name'
        for line in file:
            for word in line.split():
                if say1 == word :
                    plit1 = line.split().index(say1)
                    after1 = line.split()[5:6]
                if say2 == word : 
                    plit2 = line.split().index(say2)
                    after2 = line.split()[5:6]
                    xs[i]=after2
                    i=i+1
    os.mkdir(after1[0])
    root_path = os.path.realpath(after1[0])
    for i in range(3):
        path = os.path.join(root_path, xs[i][0])
        os.mkdir(path)

args = parse_args()
creat(args.schema)