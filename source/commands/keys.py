from abc import ABC
import os
class keys(ABC):
    DB_NAME = "database_name"
    TABLES  = "Tables"
    NAME = "name"
    COLUMNS = "columns"
    PK = "primary_key"
    IDX_KEY = "Index_keys"
    CONSISTENCY = "Consistency"
    SCHEMA = os.path.join(str(os.getcwd()).replace("commands","").replace("source" ,"").replace("tests", ""),'tests') 