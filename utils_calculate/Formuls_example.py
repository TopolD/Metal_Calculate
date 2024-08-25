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
        return self.clean_data(self.db.Fuse.get(Tcn=self.Tcn))

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

    @staticmethod
    def __calculate_data(data: dict, element):
        fuse_element = float(data['Fuse'][element])
        samples_element = float(data['Samples'][element])
        materials_element = float(data['Materials'][element][element])
        multiplied_w = float(data['W']) * 1000

        return (fuse_element - samples_element) * (multiplied_w / materials_element)

    def remainder_material(self):
        instance = self.Data_fuse['Materials'].items()
        for attr_key, attr_value in instance:
            material_type = self.Data_fuse['Materials'][attr_key]
            for element_key, element_value in material_type.items():
                if element_key != attr_key:
                    if element_key == 'C':
                        return self.remainder_materials_all(attr_key, element_key)

                    if element_key == 'Si':
                        return self.remainder_materials_all(attr_key, element_key)

    @staticmethod
    def calculate_remainder_material(data: dict, material, element, residue):
        multiplied_w = float(data['W']) * 1000
        materials_element = float(data['Materials'][element][residue])
        value = float(data['Materials'][residue][residue])
        return (material / multiplied_w) * (materials_element / value) * multiplied_w

    def remainder_materials_all(self, element, material):
        instance = self.__calculate_data(self.Data_fuse, material)
        Mn = self._calculate_materials_mn()
        if element:
            if element == 'Mn':
                result_mn = self.calculate_remainder_material(self.Data_fuse, Mn, element, material)
                result = instance - result_mn
                return result
            if element == 'Cr':
                Cr = self.__calculate_data(self.Data_fuse, 'Cr')
                result_mn = self.calculate_remainder_material(self.Data_fuse, Mn, element, material)
                result_cr = self.calculate_remainder_material(self.Data_fuse, Cr, element, material)
                result = instance - (result_mn + result_cr)
                return result

    def _calculate_materials_c(self):
        if self.Data_fuse['Materials']['Mn']['C']:
            return self.remainder_material()
        return self.__calculate_data(self.Data_fuse, 'C')

    def _calculate_materials_si(self):
        if self.Data_fuse['Materials']['Mn']['Si']:
            return self.remainder_material()
        return self.__calculate_data(self.Data_fuse, 'Si')

    def _calculate_materials_mn(self):
        return self.__calculate_data(self.Data_fuse, 'Mn')

    def _calculate_materials_cr(self):
        return self.__calculate_data(self.Data_fuse, 'Cr')

    def _calculate_materials_ni(self):
        return self.__calculate_data(self.Data_fuse, 'Ni')

    def _calculate_materials_cu(self):
        return self.__calculate_data(self.Data_fuse, 'Cu')

    def _calculate_materials_mo(self):
        return self.__calculate_data(self.Data_fuse, 'Mo')

    def _calculate_materials_v(self):
        return self.__calculate_data(self.Data_fuse, 'V')

    def _calculate_materials_nb(self):
        return self.__calculate_data(self.Data_fuse, 'Nb')
