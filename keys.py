from abc import ABCMeta

<<<<<<< Updated upstream:keys.py
class keys(metaclass=ABCMeta):
=======
class keys(metaclass=ABCMeta): 
>>>>>>> Stashed changes:Keys.py
    schema = "schema"
    DB_Name = "database_name"
    tables  = "Tables"
    name = "name"
    columns = "columns"
    pk = "primary_key"
    idx_key = "Index_keys"
    consistency = "Consistency"