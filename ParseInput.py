import argparse
def parse_args():
    parser= argparse.ArgumentParser ()
    parser.add_argument (
        "-cmd",
        "--command",
        type=str,
        choices=["create","set","get","delete"],
        help= "Commands are Create, Set, Get, Delete")

    parser.add_argument ("-db_Name",
        "--Database_Name",
        type=str,
        help= "Database Name")

    parser.add_argument ("-sc",
        "--schema",
        type=str,
        help= "This is the Database schema")

    parser.add_argument("-tb",
        "--table",
        type=str,
        help="Table Name")

    parser.add_argument("-v",
        "--value",
        type=str,
        help="This is the value to be set")

    parser.add_argument(
        "-pk",
        "--primary_key",
        type=str,
        help="Primary key is a unique key")
    
    return parser.parse_args()