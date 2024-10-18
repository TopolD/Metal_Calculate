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
        self.FuseDataTarget()
        self.AbsorptionRateData()
        self.CoredWireData()

    def AbsorptionRateData(self):
        class AbsorptionRate(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            AbrName = Required(str)
            C = Optional(float)
            Mn = Optional(float)
            Si = Optional(float)
            Cr = Optional(float)
            Ti = Optional(float)
            V = Optional(float)
            Mo = Optional(float)
            B = Optional(float)
            Nb = Optional(float)
            Ni = Optional(float)
            Cu = Optional(float)
            Al = Optional(float)
            S = Optional(float)
            Fe = Optional(float)
            Ca = Optional(float)
            P = Optional(float)

        self.AbsorptionRate = AbsorptionRate

    def ChemicalData(self):
        class ChemicalComposition(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            MaterialName = Required(str)
            C = Optional(float)
            Mn = Optional(float)
            Si = Optional(float)
            Cr = Optional(float)
            Ti = Optional(float)
            V = Optional(float)
            Mo = Optional(float)
            B = Optional(float)
            Nb = Optional(float)
            Ni = Optional(float)
            Cu = Optional(float)
            Al = Optional(float)
            S = Optional(float)
            Fe = Optional(float)
            Ca = Optional(float)
            P = Optional(float)

        self.ChemicalComposition = ChemicalComposition

    def FuseData(self):
        class Fuse(self.db.Entity):

            Tcn = Required(str)
            FuseName = Required(str)
            TempVd = Required(str)
            Temp_ccm1 = Required(str)
            Temp_ccm2 = Required(str)
            TargetForFuse= Optional('FuseTarget')

        self.Fuse = Fuse

    def FuseDataTarget(self):
        class FuseTarget(self.db.Entity):
            Fuse = Required('Fuse')
            Tcn = PrimaryKey(str)
            C = Optional(float)
            Mn = Optional(float)
            Si = Optional(float)
            Cr = Optional(float)
            Ti = Optional(float)
            V = Optional(float)
            Mo = Optional(float)
            B = Optional(float)
            Nb = Optional(float)
            Ni = Optional(float)
            Cu = Optional(float)
            Al = Optional(float)
            S = Optional(float)
            Ca = Optional(float)
            Cpr = Optional(float)

        self.FuseTarget = FuseTarget

    def CoredWireData(self):
        class CoredWire(self.db.Entity):
            ID = PrimaryKey(int, auto=True)
            CWName = Required(str)
            C = Optional(float)
            Mn = Optional(float)
            Si = Optional(float)
            Cr = Optional(float)
            Ti = Optional(float)
            V = Optional(float)
            Mo = Optional(float)
            B = Optional(float)
            Nb = Optional(float)
            Ni = Optional(float)
            Cu = Optional(float)
            Al = Optional(float)
            S = Optional(float)
            Fe = Optional(float)
            Ca = Optional(float)
            P = Optional(float)

        self.CoredWire = CoredWire

    def reset_database(self):
        self.db.drop_all_tables(with_all_data=True)
        self.db.create_tables()
