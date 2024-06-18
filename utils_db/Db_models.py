from pony.orm import *


class ConnDb():
    def __init__(self):
        self.db = Database()
        self.db.bind(provider='sqlite', filename='Fuse.db', create_db=True)
        set_sql_debug(True)
        self.FuseData()
        self.db.generate_mapping(create_tables=True)

    def FuseData(self):
        class Fuse(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            FuseName = Required(str)
            Tcn = Required(int)
            TempVd = Required(int)
            Temp_ccm1 = Required(int)
            Temp_ccm2 = Required(int)
            C = Required(float)
            Si = Required(float)
            Mn = Required(float)
            S = Optional(float)
            Al = Optional(float)
            Cr = Optional(float)
            Mo = Optional(float)
            Ni = Optional(float)
            Cu = Optional(float)
            V = Optional(float)
            Nb = Optional(float)
            Ti = Optional(float)
            B = Optional(float)
            Ca = Optional(float)
            Cpr = Optional(float)

        self.Fuse = Fuse

    def reset_database(self):
        self.db.drop_all_tables(with_all_data=True)
        self.db.create_tables()
