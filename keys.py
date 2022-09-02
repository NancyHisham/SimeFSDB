from abc import ABCMeta

class keys(metaclass=ABCMeta):
    schema = "schema"
    DB_Name = "database_name"
    tables  = "Tables"
    name = "name"
    columns = "columns"
    pk = "primary_key"
    idx_key = "Index_keys"
    consistency = "Consistency"
