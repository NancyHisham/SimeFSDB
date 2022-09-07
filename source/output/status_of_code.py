from enum import Enum

class StatusOfCode(Enum):
    Success = 0
    NoParameterError = 1
    NoCommandEntered = 2
    WrongCommandError=3
    SchemaNotFound = 4
    ErrorLoadingJsonFile = 5
    DatabaseNameMissing = 6

