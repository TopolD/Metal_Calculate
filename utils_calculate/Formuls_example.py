from pony.orm import *
from utils_db.Db_models import ConnDb


class DataHolder:
    Tcn = None
    Data = None

    @classmethod
    def set_data(cls, Tcn, Data):
        cls.Tcn = Tcn
        cls.Data = Data


class GetDataCalculate:

    def __init__(self):
        self.db = ConnDb()
        self.Tcn = DataHolder.Tcn
        self.Data = DataHolder.Data

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

    def gather_materials(self):
        data_for_fuse = {}

        Fuse = self.get_data_fuse()
        Samples = self.get_samples()
        Materials = self.get_material()

        data_for_fuse.update({
            'W': self.Data.get('W'),
            "Fuse": Fuse,
            'Samples': Samples,
            'Materials': Materials
        })
        return data_for_fuse


class Calculate(GetDataCalculate):

    def __init__(self):
        super().__init__()
        self.Data_fuse = self.gather_materials()

    def __get_formula_result(self, name):
        return self.__calculate_data(self.Data_fuse, name)

    @staticmethod
    def __calculate_data(Data: dict, element):
        return (float(Data.get('Fuse').get(element)) - (float(Data.get('Samples').get(element)))) * (float(
            Data.get('W') * 1000) / (float(
            Data.get('Materials').get(element).get(element))))


    @staticmethod


    def _calculate_materials_c(self):
        return self.__get_formula_result('C')

    def _calculate_materials_si(self):
        return self.__get_formula_result('Si')

    def _calculate_materials_mn(self):
        return self.__get_formula_result('Mn')
