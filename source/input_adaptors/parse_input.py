import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(
        "-command",
        "--cmd",
        type=str,
        help= "Command : Create , Get , Set , Delete",
    )
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
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="The Database name",
    )
    parser.add_argument(
        "-tb",
        "--table",
        type=str,
        help="The Table name",
    )
    parser.add_argument(
        "-val",
        "--value",
        type=str,
        help="The Value to add",
    )
    parser.add_argument(
        "-p",
        "--parameter",
        type=str,
        help="Parameter desired to be set",
    )
    return parser.parse_args()



         

