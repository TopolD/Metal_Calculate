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
            if self.GetDataAbsorCoef(Data.get('NameMn')).C and self.GetDataAbsorCoef(Data.get('NameMn')).Si:
                Weight = Data.get('W') * 1000

                Mn = (((float(Fuse.get('Mn')) - Data.get('Mn')) * Weight)
                      / float(self.GetDataAbsorCoef(Data.get('NameMn')).Mn))

                GetCWithMn = Mn / Weight * float(self.GetDataAbsorCoef(Data.get('NameMn')).C)
                GetSiWithMn = Mn / Weight * float(self.GetDataAbsorCoef(Data.get('NameMn')).Si)

                Si = (((float(Fuse.get('Si')) - Data.get('Si') - GetSiWithMn) * Weight)
                      / float(self.GetDataAbsorCoef(Data.get('NameSi')).Si))
                if Fuse.get('Cr'):
                    Cr = (((float(Fuse.get('Cr')) - Data.get('Cr')) * Weight)
                          / float(self.GetDataAbsorCoef(Data.get('NameCr')).Cr))
                    GetCWithCr = (Cr / Weight * (float(self.GetDataAbsorCoef(Data.get('NameCr')).C) + float(
                        self.GetDataAbsorCoef(Data.get('NameMn')).C)))
                    C = (((float(Fuse.get('C')) - Data.get('C') - (GetCWithMn + GetCWithCr)) * Weight)
                         / float(self.GetDataAbsorCoef(Data.get('NameC')).C))
                    materials.update({
                        'Cr': int(Cr)
                    })
                else:
                    C = (((float(Fuse.get('C')) - Data.get('C') - GetCWithMn) * Weight)
                         / float(self.GetDataAbsorCoef(Data.get('NameC')).C))
                materials.update({
                    'C': int(C),
                    'Si': int(Si),
                    'Mn': int(Mn),

                })
                return materials
