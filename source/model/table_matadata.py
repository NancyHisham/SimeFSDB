import json
import os
from model.index import *
from commands.keys import *
from output.exceptions import *


class TableMetadata:
    def __init__(self, table_map, path):
        self.table_map = table_map
        self.path = os.path.join(path, self.table_map[keys.NAME])
        self.__validate__(self)
        self.serialize()

    def serialize(self):
        os.makedirs(self.path, exist_ok=True)
        with open(os.path.join(self.path, "{}.json".format(self.table_map[keys.NAME])), 'w') as file:
            json.dump(self.table_map, file)
        self.__create_indices__(self)

    @staticmethod
    def __create_indices__(self):
        for index in self.table_map[keys.IDX_KEY]:
            index = Index(index, self.table_map, self.path)
            index.create()

    def __validate__(self):
        if self.table_map[keys.PK] is None or self.table_map[keys.PK] not in self.table_map[keys.COLUMNS]:
            raise WrongCommandError("Primary_key {} is not found".format(keys.PK))