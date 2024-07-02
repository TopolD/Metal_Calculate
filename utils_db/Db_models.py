from pony.orm import *


class ConnDb:
    def __init__(self):
        self.db = Database()
        self.db.bind(provider='sqlite', filename='Fuse.db', create_db=True)

        # set_sql_debug(True)

        self.ModelsData()

        self.db.generate_mapping(create_tables=True)

    def ModelsData(self):
        self.ChemicalData()
        self.FuseData()
        self.AbsorptionRateData()
        self.CoredWireData()

    def AbsorptionRateData(self):
        class AbsorptionRate(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            AbrName = Required(str)
            C = Optional(str)
            Mn = Optional(str)
            Si = Optional(str)
            Cr = Optional(str)
            Ti = Optional(str)
            V = Optional(str)
            Mo = Optional(str)
            B = Optional(str)
            Nb = Optional(str)
            Ni = Optional(str)
            Cu = Optional(str)
            Al = Optional(str)
            S = Optional(str)
            Fe = Optional(str)
            Ca = Optional(str)
            P = Optional(str)

        self.AbsorptionRate = AbsorptionRate

    def ChemicalData(self):
        class ChemicalComposition(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            MaterialName = Required(str)
            C = Optional(str)
            Mn = Optional(str)
            Si = Optional(str)
            Cr = Optional(str)
            Ti = Optional(str)
            V = Optional(str)
            Mo = Optional(str)
            B = Optional(str)
            Nb = Optional(str)
            Ni = Optional(str)
            Cu = Optional(str)
            Al = Optional(str)
            S = Optional(str)
            Fe = Optional(str)
            Ca = Optional(str)
            P = Optional(str)

        self.ChemicalComposition = ChemicalComposition

    def FuseData(self):
        class Fuse(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            Tcn = Required(str)
            FuseName = Required(str)
            TempVd = Required(str)
            Temp_ccm1 = Required(str)
            Temp_ccm2 = Required(str)
            C = Required(str)
            Si = Required(str)
            Mn = Required(str)
            S = Optional(str)
            Al = Optional(str)
            Cr = Optional(str)
            Mo = Optional(str)
            Ni = Optional(str)
            Cu = Optional(str)
            V = Optional(str)
            Nb = Optional(str)
            Ti = Optional(str)
            B = Optional(str)
            Ca = Optional(str)
            Cpr = Optional(str)

        self.Fuse = Fuse

    def CoredWireData(self):
        class CoredWire(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            CWName = Required(str)
            provider = Required(str)
            CorWire = Required(str)
            weight = Required(str)

        self.CoredWire = CoredWire

    def reset_database(self):
        self.db.drop_all_tables(with_all_data=True)
        self.db.create_tables()
