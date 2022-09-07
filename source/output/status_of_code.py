from enum import Enum

class StatusOfCode(Enum):
    Success = 0
    NoCommandEntered = 1
    WrongCommandError=2
    SchemaNotFound = 3
    ErrorLoadingJsonFile = 4
    DatabaseNameMissing = 5

