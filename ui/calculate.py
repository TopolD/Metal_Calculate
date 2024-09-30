from ui.app_example import *
from utils_calculate.Formuls_example import *


class CalculationHandler(DisplayWindow):

    def __init__(self, Tcn):
        super().__init__()
        self.Calc = Calculate()
        DataHolder.set_data(Tcn, None)
        self.Fuse = GetDataCalculate().get_data_fuse()


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
        for value in instance[6:]:
            handler = self.checkvaluehandler(value)
            if handler:
                Dict_Samples.update({value: handler})
        return Dict_Samples

    def get_matching_value(self):
        return [data for data in self.DictionaryUnpacker(self.material_handlers, 'key')]

    def checkvaluehandler(self, value):
        instance = self.get_matching_value()
        for key in instance:

            if key == value:
                return self.material_handlers.get(key)()
