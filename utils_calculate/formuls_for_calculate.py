from utils_db.Db_models import ConnDb
from pony.orm import db_session


class DataHolder:
    Tcn = None
    Data = None

    @classmethod
    def set_data(cls, Tcn, Data):
        cls.Tcn = Tcn
        cls.Data = Data


class HandlerCleanData:

    def clean_data(self, DataDb):
        try:
            if DataDb:
                Clean_Data = {}
                for attr_name, attr_value in DataDb.to_dict().items():
                    if attr_value != 0.0:
                        Clean_Data[attr_name] = attr_value
                return Clean_Data
        except Exception as e:
            print(e)
        self.clean_data(DataDb)


class get_data_calculate_with_db:

    def __init__(self):

        self.db = ConnDb()
        self.Tcn = DataHolder.Tcn
        self.Data = DataHolder.Data

    @db_session
    def get_data_fuse(self):
        return HandlerCleanData().clean_data(self.db.Fuse.get(Tcn=self.Tcn))

    @db_session
    def get_data_target_for_fuse(self):
        Target_Data = HandlerCleanData().clean_data(self.db.FuseTarget.get(Tcn=self.Tcn))
        stark_key = 'C'
        Sliced_Dict = {}
        take = False
        for attrkey, attrvalue in Target_Data.items():
            if attrkey == stark_key:
                take = True
            if take:
                Sliced_Dict[attrkey] = attrvalue
        return Sliced_Dict

    @db_session
    def get_material(self):

        Material_dict = self.Data['material']
        Material = {}

        if Material_dict:
            for value_atr, value_name in Material_dict.items():
                raw_result = self.db.ChemicalComposition.get(MaterialName=value_name)
                if raw_result:
                    result = HandlerCleanData().clean_data(raw_result)
                    filtered_result = {k: v for k, v in result.items() if k not in ('ID', 'MaterialName')}
                    Material[value_atr] = filtered_result
            return Material


class data_for_calculate(get_data_calculate_with_db):

    def __init__(self):
        super().__init__()

    def gather_materials(self):
        data_for_fuse = {}

        Fuse = self.get_data_fuse()
        Samples = self.Data['samples']
        Materials = self.get_material()
        CoreWire = self.Data['corewire']

        data_for_fuse.update({
            'W': self.Data.get('W'),
            "Fuse": Fuse,
            'Samples': Samples,
            'Materials': Materials,
            'corewire': CoreWire,
        })
        return data_for_fuse


class calculate_remainder_material:

    def __init__(self):
        super().__init__()
        self.Data_fuse = data_for_calculate().gather_materials()

    @staticmethod
    def __calculate_data(data: dict, element):
        fuse_element = data['Fuse'][element]
        samples_element = data['Samples'][element]
        materials_element = data['Materials'][element][element]
        multiplied_w = float(data['W']) * 1000

        return (fuse_element - samples_element) * (multiplied_w / materials_element)

    def remainder_material(self, value):
        instance = self.Data_fuse['Materials'].items()
        for attr_key, attr_value in instance:
            material_type = self.Data_fuse['Materials'][attr_key]
            for element_key, element_value in material_type.items():
                if element_key != attr_key:
                    if element_key == value:
                        if element_key == 'C':
                            return self.remainder_materials_all(attr_key, element_key)

                        if element_key == 'Si':
                            return self.remainder_materials_all(attr_key, element_key)

    @staticmethod
    def calculate_remainder_material(data: dict, material, element, residue):
        multiplied_w = float(data['W']) * 1000
        materials_element = data['Materials'][element][residue]
        value = data['Materials'][residue][residue]
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
            return round(self.remainder_material('C'), 1)
        return round(self.__calculate_data(self.Data_fuse, 'C'), 1)

    def _calculate_materials_si(self):
        if self.Data_fuse['Materials']['Mn']['Si']:
            return round(self.remainder_material('Si'), 1)
        return round(self.__calculate_data(self.Data_fuse, 'Si'), 1)

    def _calculate_materials_mn(self):
        return round(self.__calculate_data(self.Data_fuse, 'Mn'), 1)

    def _calculate_materials_cr(self):
        return round(self.__calculate_data(self.Data_fuse, 'Cr'), 1)

    def _calculate_materials_ni(self):
        return round(self.__calculate_data(self.Data_fuse, 'Ni'), 1)

    def _calculate_materials_cu(self):
        return round(self.__calculate_data(self.Data_fuse, 'Cu'), 1)

    def _calculate_materials_mo(self):
        return round(self.__calculate_data(self.Data_fuse, 'Mo'), 1)

    def _calculate_materials_v(self):
        return round(self.__calculate_data(self.Data_fuse, 'V'), 1)

    def _calculate_materials_nb(self):
        return round(self.__calculate_data(self.Data_fuse, 'Nb'), 1)

    def _calculate_materials_b(self):
        return round(self.__calculate_data(self.Data_fuse, 'B'), 1)


class calculate_core_wire():

    def __init__(self):
        super().__init__()
        self.Data_fuse_for_cire = data_for_calculate().gather_materials()

    def calculate_core_wire(self, material):
        target_value = float(self.Data_fuse_for_cire['Fuse'][material])
        W = float(self.Data_fuse_for_cire['W'])
        coef = self.calculate_coef()
        samples_core_wire = float(self.Data_fuse_for_cire['corewire'][material])
        return (target_value - samples_core_wire) * W / float(coef[material])

    def calculate_coef(self):
        material_core_coef = {
            'Al': 24,
            'Ti': 20.8,
            'C': 16
        }
        return material_core_coef
