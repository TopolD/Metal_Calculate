import unittest
from .Db_models import *


class TestFuseDb(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn_db = ConnDb()
        cls.conn_db.reset_database()

    def setUp(self):
        self.conn_db.reset_database()

    @db_session
    def test_create_record(self):
        NewFuse = self.conn_db.Fuse(
            FuseName='FuseName',
            Tc='1',
            TempV='1',
            Temp_ccm1='1',
            Temp_ccm2='1',
            Tar
        )
        commit()
        self.assertIsNotNone(NewFuse.ID)

    # @db_session
    # def test_create_record(self):
    #     NewChemicalData = self.conn_db.ChemicalComposition(
    #         MaterialName='1',
    #         C='1',
    #         Si='1',
    #         Mn='1',
    #         Cr='1',
    #         Ti='1',
    #         V='1',
    #         Mo='1',
    #         Nb='1',
    #         Ni='1',
    #         Cu='1',
    #         Al='1',
    #         S='1',
    #         Fe='1',
    #         Ca='1',
    #         P='1'
    #     )
    #     commit()
    #     self.assertIsNotNone(NewChemicalData.ID)
    #
    # @db_session
    # def test_create_record(self):
    #     NewAbsorptionRate = self.conn_db.AbsorptionRate(
    #         AbrName='1',
    #         C='1',
    #         Si='1',
    #         Mn='1',
    #         Cr='1',
    #         Ti='1',
    #         V='1',
    #         Mo='1',
    #         B='1',
    #         Nb='1',
    #         Ni='1',
    #         Cu='1',
    #         Al='1',
    #         S='1',
    #         Fe='1',
    #         Ca='1',
    #         P='1'
    #     )
    #     commit()
    #     self.assertIsNotNone(NewAbsorptionRate.ID)


if __name__ == "__main__":
    unittest.main()
