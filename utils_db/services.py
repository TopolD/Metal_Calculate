from pony.orm import db_session
from utils_db.Db_models import ConnDb


class CreateServices:

    def __init__(self):
        self.db = ConnDb()

    def CreateAbsorptionRateEntity(self, DictData):
        with db_session:
            try:
                NewAbsorptionRate = self.db.AbsorptionRate(
                    AbrName=DictData.get('AbrName'),
                    C=DictData.get('C'),
                    Mn=DictData.get('Mn'),
                    Si=DictData.get('Si'),
                    Cr=DictData.get('Cr'),
                    Ti=DictData.get('Ti'),
                    V=DictData.get('V'),
                    Mo=DictData.get('Mo'),
                    B=DictData.get('B'),
                    Nb=DictData.get('Nb'),
                    Ni=DictData.get('Ni'),
                    Cu=DictData.get('Cu'),
                    Al=DictData.get('Al'),
                    S=DictData.get('S'),
                    Fe=DictData.get('Fe'),
                    Ca=DictData.get('Ca'),
                    P=DictData.get('P'),
                )
                print(f' Created AbsorptionRate {NewAbsorptionRate}')
            except Exception as e:
                pass

    def CreateChemicalCompositionEntity(self, DictData):
        with db_session:
            try:
                NewChemicalComposition = self.db.ChemicalComposition(
                    MaterialName=DictData.get('MaterialName'),
                    C=DictData.get('C'),
                    Mn=DictData.get('Mn'),
                    Si=DictData.get('Si'),
                    Cr=DictData.get('Cr'),
                    Ti=DictData.get('Ti'),
                    V=DictData.get('V'),
                    Mo=DictData.get('Mo'),
                    Nb=DictData.get('Nb'),
                    Ni=DictData.get('Ni'),
                    Cu=DictData.get('Cu'),
                    Al=DictData.get('Al'),
                    S=DictData.get('S'),
                    Fe=DictData.get('Fe'),
                    Ca=DictData.get('Ca'),
                    P=DictData.get('P'),
                )
                print(f' Created ChemicalComposition {NewChemicalComposition}')
            except Exception as e:
                pass

    def CreateFuseEntity(self, DictData):
        with db_session:
            try:
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
            except Exception as e:
                pass

    def CreateCoredWireEntity(self, DictData):
        with db_session:
            try:
                NewCoreWire = self.db.CoredWire(
                    CWName=DictData.get('CWName'),
                    provider=DictData.get('provider'),
                    CorWire=DictData.get('CorWire'),
                    weight=DictData.get('weight')
                )
                print(f' Created CoreWire {NewCoreWire}')
            except Exception as e:
                pass


class DeleteServices(CreateServices):
    pass


class UpdateServices:
    pass
