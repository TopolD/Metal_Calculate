from pony.orm import *

from utils_db.Db_models import ConnDb


class WorkWithEntityInstances:

    def __init__(self, NameDb):
        self.db = ConnDb()
        self.cm = commit()
        self.NameDb = NameDb

    def CreatingEntity(self, *args: str):
        with db_session:
            if self.NameDb == self.db.Fuse._table_:
                if len(args) == 20:
                    NewFuse = self.db.Fuse(
                        Tcn=args[0],
                        FuseName=args[1],
                        TempVd=args[2],
                        Temp_ccm1=args[3],
                        Temp_ccm2=args[4],
                        C=args[5],
                        Si=args[6],
                        Mn=args[7],
                        S=args[8],
                        Al=args[9],
                        Cr=args[10],
                        Mo=args[11],
                        Ni=args[12],
                        Cu=args[13],
                        V=args[14],
                        Nb=args[15],
                        Ti=args[16],
                        B=args[17],
                        Ca=args[18],
                        Cpr=args[19],

                    )
                    print(f' Created Fuse {NewFuse}')
                else:
                    print(f"Dont created Fuse ")

    def DeleteEntity(self, FuseName):
        with db_session:
            if self.NameDb == self.db.Fuse._table_:
                Fuse = self.db.Fuse.get(FuseName=FuseName).delete()
                print(f' Deleted Fuse {FuseName}')
                return True

    def UpdateEntity(self):
        pass
