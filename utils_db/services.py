from pony.orm import db_session

from utils_db.Db_models import ConnDb


class Services:

    def __init__(self):
        self.db = ConnDb()

    def CreateFuseEntity(self, DictData):
        with db_session:
            NewFuse = self.db.Fuse(
                Tcn=DictData.get('Tcn'),
                FuseName=DictData.get('FuseName'),
                TempVd=DictData.get('TempVd'),
                Temp_ccm1=DictData.get('Temp_ccm1'),
                Temp_ccm2=DictData.get('Temp_ccm2'),
                C=DictData.get('C'),
                Si=DictData.get('Si'),
                Mn=DictData.get('Mn'),
                S=DictData.get('S'),
                Al=DictData.get('Al'),
                Cr=DictData.get('Cr'),
                Mo=DictData.get('Mo'),
                Ni=DictData.get('Ni'),
                Cu=DictData.get('Cu'),
                V=DictData.get('V'),
                Nb=DictData.get('Nb'),
                Ti=DictData.get('Ti'),
                B=DictData.get('B'),
                Ca=DictData.get('Ca'),
                Cpr=DictData.get('Cpr'),
            )

            print(f' Created Fuse {NewFuse}')

    def CreateAbsorptionRateEntity(self):
        pass

    def CreateChemicalCompositionEntity(self):
        pass

    def CreateCoredWireEntity(self):
        pass
