from pony.orm import *
from utils_db.Db_models import ConnDb


class GetDataCalculate:

    def __init__(self, tcn):
        self.db = ConnDb()
        self.Tcn = tcn

    @db_session
    def GetDataFuse(self):
        instance = self.db.Fuse.get(Tcn=self.Tcn)
        CleanFuse = {}
        if instance:
            for attr_name, attr_value in instance.to_dict().items():
                if not self.is_nan(attr_value) and attr_value is not None:
                    CleanFuse[attr_name] = attr_value
            return CleanFuse

    @staticmethod
    def is_nan(value):
        try:
            import math
            return math.isnan(float(value))
        except (ValueError, TypeError):
            return False

    @db_session
    def GetDataAbsorCoef(self, Material_name):
        Material = self.db.ChemicalComposition.get(MaterialName=Material_name)
        return Material

    @db_session
    def GetBaseDataMaterial(self, Data: dict):
        Fuse = self.GetDataFuse()
        materials = {}

        if Fuse:
            Weight = Data.get('W') * 1000
            C = (((float(Fuse.get('C')) - Data.get('C')) * Weight)
                 / float(self.GetDataAbsorCoef(Data.get('NameC')).C))
            Si = (((float(Fuse.get('Si')) - Data.get('Si')) * Weight)
                  / float(self.GetDataAbsorCoef(Data.get('NameSi')).Si))
            Mn = (((float(Fuse.get('Mn')) - Data.get('Mn')) * Weight)
                  / float(self.GetDataAbsorCoef(Data.get('NameMn')).Mn))
            if self.GetDataAbsorCoef(Data.get('NameMn')).C and self.GetDataAbsorCoef(Data.get('NameMn')).Si:
                C -= (Mn * float(self.GetDataAbsorCoef(Data.get('NameMn')).C)) / 100
                Si -= (Mn * float(self.GetDataAbsorCoef(Data.get('NameMn')).Si)) / 100

            materials.update({
                'C': int(C),
                'Si': int(Si),
                'Mn': int(Mn)

            })
            return materials
