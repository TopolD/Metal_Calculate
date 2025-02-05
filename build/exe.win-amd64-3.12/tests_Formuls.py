import unittest
from utils_calculate.formuls_for_calculate import DataHolder, GetDataCalculateWithDb, CalculateRemainderMaterial, \
    DataForCalculate
from utils_db.Db_models import ConnDb


class TestDataHolder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = ConnDb()
        cls.DataHolder = DataHolder()

    def test_set_data(self):
        self.DataHolder.set_data('26', Data={
            'W': '160',
            'material': {
                'C': 'GKA',
                'Si': 'FeSi75',
                'Mn': 'SiMn17'
            },
            'samples': {
                'C': 0,
                'Si': 0,
                'Mn': 0,
            },
            'corewire': {}
        }
                                 )


class TestGetDataMaterial(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = ConnDb()
        DataHolder().set_data('26', Data={
            'W': '160',
            'material': {
                'C': 'GKA',
                'Si': 'FeSi75',
                'Mn': 'SiMn17'
            },
            'samples': {
                'C': 0,
                'Si': 0,
                'Mn': 0,
            },
            'corewire': {}
        }
                              )
        cls.GetData = GetDataCalculateWithDb()

    def test_get_data_material(self):
        Material_Data = self.GetData.get_material()
        self.assertIsNotNone(Material_Data, 'Material_Data isn"t None')

    def test_get_data_fuse(self):
        Fuse_Data = self.GetData.get_data_fuse()
        self.assertIsNotNone(Fuse_Data, 'Fuse_Data isn"t None')


class TestCalculateRemainderMaterial(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = ConnDb()
        DataHolder().set_data('26', Data={
            'W': '160',
            'material': {
                'C': 'GKA',
                'Si': 'FeSi75',
                'Mn': 'SiMn17'
            },
            'samples': {
                'C': 0,
                'Si': 0,
                'Mn': 0,
            },
            'corewire': {}
        })
        cls.GetData = GetDataCalculateWithDb()
        cls.Calc = CalculateRemainderMaterial()

    def test_calculate_materials(self):
        Samples = DataForCalculate().gather_materials()

        Dict_calc_material = {
            'C': self.Calc._calculate_materials_c,
            'Si': self.Calc._calculate_materials_si,
            'Mn': self.Calc._calculate_materials_mn,
        }

        for attr_key, attr_value in Dict_calc_material.items():
            if Samples['Samples'][attr_key]:
                self.assertIsNotNone(attr_value())



if __name__ == "__main__":
    unittest.main()
