import argparse
from email import parser

def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(

        "-cmd",
        "--command",
        type=str,
        help= "Command : Create , Get , Set , Delete",
    )
<<<<<<< Updated upstream
    parser.add_argument(
=======
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



         

