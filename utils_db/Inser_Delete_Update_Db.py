from pony.orm import *
from utils_db.Db_models import ConnDb
from utils_db.services import Services


class WorkWithEntityInstances:

    def __init__(self):
        self.db = ConnDb()
        self.sv = Services()

    def CreatingEntity(self, NameDb: str, DictData: dict):
            if NameDb == 'Fuse':
                return self.sv.CreateFuseEntity(DictData)

    def DeleteEntity(self, FuseName):
        with db_session:
            if self.NameDb == self.db.Fuse._table_:
                Fuse = self.db.Fuse.get(FuseName=FuseName).delete()
                print(f' Deleted Fuse {FuseName}')
                return True

    def UpdateEntity(self):
        with db_session:
            if self.NameDb == self.db.Fuse._table_:
                pass
