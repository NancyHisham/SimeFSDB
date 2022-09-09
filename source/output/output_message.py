import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from output.exceptions import * 
from output.status_of_code import StatusOfCode

class OutputMessage:
    def __init__(self, command_name, result, exception):
        self.result = result
        self.status = StatusOfCode.Success.value if exception is None else exception.status_code
        self.message = str(command_name + " is done successfully") if exception is None else str(exception)
        
        