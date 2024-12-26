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

        Fuse_Elements = self.get_data_target_for_fuse()
        Samples = self.Data['samples']
        Materials = self.get_material()
        CoreWire = self.Data['corewire']
        Temp = self.Data['temp']

        data_for_fuse.update({
            'W': self.Data.get('W'),
            "Fuse": Fuse_Elements,
            'Samples': Samples,
            'Materials': Materials,
            'corewire': CoreWire,
            'temp': Temp
        })
        return data_for_fuse


class remainder_calculata_material:

    def __init__(self):
        self.Data_Fuse = data_for_calculate().gather_materials()

    def handler_remainder_material(self):
        remainder_dict_value = {}

        materials = self.Data_Fuse['Materials']
        for attr_key, attr_value in materials.items():
            for attr_key_value, attr_value_key in attr_value.items():
                if attr_key != attr_key_value:
                    if attr_key not in remainder_dict_value:
                        remainder_dict_value[attr_key] = {}

                    remainder_dict_value[attr_key][attr_key_value] = attr_value_key

        return remainder_dict_value

    def calculate_remainder_material(self, material, calculate_materials):
        instance = self.handler_remainder_material()

        result = calculate_materials

        for attr_key, attr_value in instance.items():

            if attr_value.get(material):
                init_material_attr_key = f'_calculate_materials_{attr_key.lower()}'
                func_material_attr_key = getattr(calculate_material(), init_material_attr_key)()

                result -= (((func_material_attr_key * attr_value[material]) / float(self.Data_Fuse.get('W'))) * float(
                    self.Data_Fuse.get('W'))) / float(self.Data_Fuse.get('Materials').get(material).get(material))
        return result


class calculate_material:

    def __init__(self):
        super().__init__()
        self.Data_fuse = data_for_calculate().gather_materials()

    @staticmethod
    def __calculate_data(data: dict, element):
        fuse_element = data['Fuse'][element]
        samples_element = float(data['Samples'][element].replace(',', '.'))
        materials_element = data['Materials'][element][element]
        multiplied_w = float(data['W']) * 1000

        return (fuse_element - samples_element) * (multiplied_w / materials_element)

    def _calculate_materials_c(self):
        return round(remainder_calculata_material().calculate_remainder_material('C', round(
            self.__calculate_data(self.Data_fuse, 'C'), 1)), 1)

    def _calculate_materials_si(self):
        return round(remainder_calculata_material().calculate_remainder_material('Si', round(
            self.__calculate_data(self.Data_fuse, 'Si'), 1)), 1)

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
        self.Data_fuse_for_core = data_for_calculate().gather_materials()
        self.Data = DataHolder.Data

    def calculate_core_wire(self, material):
        target_value = float(self.Data_fuse_for_core['Fuse'][material])
        W = float(self.Data_fuse_for_core['W'])
        coef = self.calculate_coef()
        samples_core_wire = float(self.Data_fuse_for_core['corewire'][material].replace(',', '.'))
        return (((target_value - samples_core_wire) / float(coef[material])) * (W * 1000 / (160 * 1000))) * 100

    def calculate_coef(self):
        material_core_coef = {
            'Al': 0.015,
            'Ti': 0.013,
            'Cpr': 0.01
        }
        return material_core_coef

    def _calculate_core_wire_c(self):
        return round(self.calculate_core_wire('Cpr'), 1)

    def _calculate_core_wire_al(self):
        if self.Data.get('material').get('Ti') == 'FeTi50':
            return round(self.calculate_core_wire('Al') - self._calculate_core_wire_ti() * 0.12, 1)
        return round(self.calculate_core_wire('Al'), 1)

    def _calculate_core_wire_ti(self):
        return round(self.calculate_core_wire('Ti'), 1)

    def _calculate_core_wire_ca(self):
        S=0.01442 * float(self.Data_fuse_for_core.get('corewire').get('Ca').replace(',', '.'))
        Al =0.00686 * float(self.Data_fuse_for_core.get('Fuse').get('Al'))
        Temp = 0.000012 * (float(self.Data_fuse_for_core.get('temp')))
        W =   float(self.Data_fuse_for_core['W'])*1000
        coef = (0.25 / 0.32 / 0.4)
        return ((S+Al+Temp-0.01675)*W)/coef
