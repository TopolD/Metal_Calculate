import unittest
from pony.orm import *
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
            Tcn=999,
            TempVd=999,
            Temp_ccm1=999,
            Temp_ccm2=999,
            C=0.999,
            Si=0.999,
            Mn=0.999,
            S=0.999,
            Al=0.999,
            Cr=0.999,
            Mo=0.999,
            Ni=0.999,
            Cu=0.999,
            V=0.999,
            Nb=0.999,
            Ti=0.999,
            B=0.999,
            Ca=0.999,
            Cpr=0.999
        )
        commit()
        self.assertIsNotNone(NewFuse.ID)


if __name__ == "__main__":
    unittest.main()
