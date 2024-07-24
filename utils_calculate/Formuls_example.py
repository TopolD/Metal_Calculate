from pony.orm import *
from utils_db.Db_models import ConnDb


class GetDataCalculate:

    def __init__(self, tcn, Data: dict):
        self.db = ConnDb()
        self.Tcn = tcn
        self.Data = Data



    def clean_data(self, DataDb):
        try:
            if DataDb:
                Clean_Data = {}
                for attr_name, attr_value in DataDb.to_dict().items():
                    if not self.is_nan(attr_value) and attr_value is not None:
                        Clean_Data[attr_name] = attr_value
                return Clean_Data
        except Exception as e:
            print(e)

    @db_session
    def get_data_fuse(self):
        try:
            result=self.clean_data(self.db.Fuse(Tcn=self.Tcn))
            return result
        except Exception as e:
            print(e)

    @staticmethod
    def is_nan(value):
        try:
            import math
            return math.isnan(float(value))
        except (ValueError, TypeError):
            return False



    @db_session
    def get_material(self):
        Material_list = self.Data['material']
        Material = {}
        try:
            if Material_list:
                for value in Material_list:
                    result = self.clean_data(self.db.ChemicalComposition.get(MaterialName=value))
                    filtered_result = {k: v for k, v in result.items() if k not in ('ID', 'MaterialName')}
                    Material[value] = filtered_result
                return Material
        except Exception as e:
            print(e)

    def get_samples(self):
        Samples = self.Data['samples']
        try:
            if Samples:
                return Samples
            else:
                return 'No samples'
        except Exception as e:
            print(e)


def material_calculation(self):
    Samples = self.get_samples()
    Materials = self.get_material()
    Fuse = self.get_data_fuse()

    pass

# @db_session
# def GetDataAbsorCoef(self):
#     Materials = {}
#
#     for attr_name, attr_value in self.Data.items():
#         if attr_value == self.db.ChemicalComposition.get(MaterialName=attr_value):
#             if not self.is_nan(attr_value) and attr_value is not None:
#                 Materials[attr_value] = self.db.ChemicalComposition.get(MaterialName=attr_value)
#     return Materials


# def coefficient_of_assimilation_material(self, Material_name):
#     pass

# @db_session
# def GetBaseDataMaterial(self, Data: dict):
#     Fuse = self.GetDataFuse()
#     materials = {}
#
#     if Fuse:
#         if self.GetDataAbsorCoef(Data.get('NameMn')).C and self.GetDataAbsorCoef(Data.get('NameMn')).Si:
#             Weight = Data.get('W') * 1000
#
#             Mn = (((float(Fuse.get('Mn')) - Data.get('Mn')) * Weight)
#                   / float(self.GetDataAbsorCoef(Data.get('NameMn')).Mn))
#
#             GetCWithMn = Mn / Weight * float(self.GetDataAbsorCoef(Data.get('NameMn')).C)
#             GetSiWithMn = Mn / Weight * float(self.GetDataAbsorCoef(Data.get('NameMn')).Si)
#
#             Si = (((float(Fuse.get('Si')) - Data.get('Si') - GetSiWithMn) * Weight)
#                   / float(self.GetDataAbsorCoef(Data.get('NameSi')).Si))
#             if Fuse.get('Cr'):
#                 Cr = (((float(Fuse.get('Cr')) - Data.get('Cr')) * Weight)
#                       / float(self.GetDataAbsorCoef(Data.get('NameCr')).Cr))
#                 GetCWithCr = (Cr / Weight * (float(self.GetDataAbsorCoef(Data.get('NameCr')).C) + float(
#                     self.GetDataAbsorCoef(Data.get('NameMn')).C)))
#                 C = (((float(Fuse.get('C')) - Data.get('C') - (GetCWithMn + GetCWithCr)) * Weight)
#                      / float(self.GetDataAbsorCoef(Data.get('NameC')).C))
#                 materials.update({
#                     'Cr': int(Cr)
#                 })
#             else:
#                 C = (((float(Fuse.get('C')) - Data.get('C') - GetCWithMn) * Weight)
#                      / float(self.GetDataAbsorCoef(Data.get('NameC')).C))
#             materials.update({
#                 'C': int(C),
#                 'Si': int(Si),
#                 'Mn': int(Mn),
#
#             })
#             return materials
