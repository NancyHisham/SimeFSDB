import os, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from output.status_of_code import StatusOfCode

class NoCommandEntered(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.NoCommandEntered.name
        super().__init__(message)

class NoParameterError(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.NoCommandEntered.name
        super().__init__(message)

class WrongCommandError(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.WrongCommandError.name
        super().__init__(message)

class SchemaNotFound(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.SchemaNotFound.name
        super().__init__(message)

class ErrorLoadingJsonFile(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.ErrorLoadingJsonFile.name
        super().__init__(message)

class DatabaseNameMissing(Exception):
    def __init__(self, message):
        self.status_code = StatusOfCode.DatabaseNameMissing.name
        super().__init__(message)
