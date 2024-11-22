from utils_calculate.formuls_for_calculate import *


class CalculationHandler:

    def __init__(self, Tcn, Data):
        super().__init__()
        self.Calc = calculate_material()
        self.Core = calculate_core_wire()
        DataHolder.set_data(Tcn, Data)
        self.Fuse = get_data_calculate_with_db().get_data_target_for_fuse()
        self.Material_Fuse = Data

        self.material_handlers = {
            'C': self.Calc._calculate_materials_c,
            'Si': self.Calc._calculate_materials_si,
            'Mn': self.Calc._calculate_materials_mn,
            'Cr': self.Calc._calculate_materials_cr,
            'Ni': self.Calc._calculate_materials_ni,
            'Cu': self.Calc._calculate_materials_cu,
            'Mo': self.Calc._calculate_materials_mo,
            'V': self.Calc._calculate_materials_v,
            'Nb': self.Calc._calculate_materials_nb,
            'B': self.Calc._calculate_materials_b,

            'Cpr': self.Core._calculate_core_wire_c,
            'Al': self.Core._calculate_core_wire_al,
            'Ti': self.Core._calculate_core_wire_ti,
        }

    @staticmethod
    def DictionaryUnpacker(Dict: dict, value):
        match value:
            case 'key':
                for attr_key, attr_value in Dict.items():
                    yield attr_key
            case 'value':
                for attr_key, attr_value in Dict.items():
                    yield attr_value
            case _:
                print('value unfound')

    def DataForSamples(self):
        return [data for data in self.DictionaryUnpacker(self.Fuse, 'key')]

    def HandlerSamples(self):
        Dict_Samples = {}
        instance = self.DataForSamples()
        for value in instance:
            handler = self.check_value_handler(value)
            if handler:
                Dict_Samples.update({value: handler})
        return Dict_Samples

    def get_matching_value(self):
        return [data for data in self.DictionaryUnpacker(self.material_handlers, 'key')]

    def check_value_handler(self, value):
        instance = self.get_matching_value()
        for key in instance:

            if key == value:
                if self.Material_Fuse['corewire'].get(value) or self.Material_Fuse['samples'].get(value):
                    return self.material_handlers.get(key)()
                else:
                    pass
