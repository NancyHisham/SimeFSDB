from enum import Enum

class StatusOfCode(Enum):
    SchemaNotFound = "The json file you entered is not found"
    ErrorLoadingJsonFile = "The data in the json file could not be loaded"
    DatabaseNameIsMissing = "The database name is missing in the json file"
    success = "Successfully created a directory"