from pony.orm import *
from utils_db.Db_models import ConnDb


class GetDataCalculate:

    def __init__(self, Tcn, Data: dict):
        self.db = ConnDb()
        self.Tcn = Tcn
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
        result = self.clean_data(self.db.Fuse.get(Tcn=self.Tcn))
        return result

    @staticmethod
    def is_nan(value):
        try:
            import math
            return math.isnan(float(value))
        except (ValueError, TypeError):
            return False

    @db_session
    def get_material(self):
        Material_dict = self.Data.get('material')
        Material = {}

        if Material_dict:
            for value_atr, value_name in Material_dict.items():
                raw_result = self.db.ChemicalComposition.get(MaterialName=value_name)
                if raw_result:
                    result = self.clean_data(raw_result)
                    filtered_result = {k: v for k, v in result.items() if k not in ('ID', 'MaterialName')}
                    Material[value_atr] = filtered_result
            return Material

    def get_samples(self):
        Samples = self.Data['samples']

        if Samples:
            return Samples
        else:
            return 'No samples'

    @db_session
    def get_absr_coef(self, sourceMaterial, derivedMaterial):
        sourceMaterial = self.db.ChemicalComposition.get(MaterialName=sourceMaterial)
        CleanSourceMaterial = self.clean_data(sourceMaterial)
        derivedMaterial = CleanSourceMaterial.get(f'{derivedMaterial}')
        return derivedMaterial

    @staticmethod
    def calculate_data(element, material, fuse, samples, weight, abs_coef=0):
        return ((float(fuse.get(element)) - float(samples.get(element)) - abs_coef) * weight) / float(
            material.get(element).get(element))

    @staticmethod
    def calculate_remainder(element, material, derivedMaterial, sourceMaterial, weight):
        return derivedMaterial / weight * float(material.get(sourceMaterial).get(element))

    def material(self):
        Fuse = self.get_data_fuse()
        Samples = self.get_samples()
        Materials = self.get_material()

        result = {}

        if Fuse:
            Weight = self.Data.get('W') * 1000
            Mn = self.calculate_data('Mn', Materials, Fuse, Samples, Weight)

            Cr = self.calculate_data('Cr', Materials, Fuse, Samples, Weight)
            # переделать как-то
            CWithMn = self.calculate_remainder('C', Materials, Mn, 'Mn', Weight)
            CWithCr = self.calculate_remainder('C', Materials, Cr, 'Cr', Weight)
            CWithAll = CWithCr + CWithMn
            SiWithMn = self.calculate_remainder('Si', Materials, Mn, 'Mn', Weight)

            C = self.calculate_data('C', Materials, Fuse, Samples, Weight, CWithAll)

            Si = self.calculate_data('Si', Materials, Fuse, Samples, Weight, SiWithMn)

            result.update(
                {
                    'C': int(C),
                    'Si': int(Si),
                    'Mn': int(Mn),
                    'Cr': int(Cr)
                }
            )

        return result
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
