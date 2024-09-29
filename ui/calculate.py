from ui.app_example import DisplayWindow
from utils_calculate.Formuls_example import *


class CalculationHandler(DisplayWindow):

    def __init__(self):
        super(CalculationHandler, self).__init__()
        self.Calc = Calculate()
        DataHolder.set_data(self.lineEdit.text(), None)
        self.Fuse = GetDataCalculate.get_data_fuse()

        self.Dict_Samples = {}
        self.material_handlers = {
            'C': self.Calc._calculate_materials_c(),
            'Si': self.Calc._calculate_materials_si(),
            'Mn': self.Calc._calculate_materials_mn(),
            'Cr': self.Calc._calculate_materials_cr(),
            'Ni': self.Calc._calculate_materials_ni(),
            'Cu': self.Calc._calculate_materials_cu(),
            'Mo': self.Calc._calculate_materials_mo(),
            'V': self.Calc._calculate_materials_v(),
            'Nb': self.Calc._calculate_materials_nb(),
            'B': self.Calc._calculate_materials_b(),
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
        for value in self.DataForSamples():
            handler = self.checkvaluehandler(value)
            if handler:
                self.Dict_Samples[value] = handler()
                yield value

    def checkvaluehandler(self, value):
        return self.material_handlers.get(value)
