from pony.orm import db_session
from utils_db.Db_models import ConnDb


class CreateServices:

    def __init__(self):
        self.db = ConnDb()

    def CreateAbsorptionRateEntity(self, Data: dict):

        with db_session:
            try:
                NewAbsorptionRate = self.db.AbsorptionRate(
                    AbrName=Data.get('AbrName'),
                    C=Data.get('C'),
                    Mn=Data.get('Mn'),
                    Si=Data.get('Si'),
                    Cr=Data.get('Cr'),
                    Ti=Data.get('Ti'),
                    V=Data.get('V'),
                    Mo=Data.get('Mo'),
                    B=Data.get('B'),
                    Nb=Data.get('Nb'),
                    Ni=Data.get('Ni'),
                    Cu=Data.get('Cu'),
                    Al=Data.get('Al'),
                    S=Data.get('S'),
                    Fe=Data.get('Fe'),
                    Ca=Data.get('Ca'),
                    P=Data.get('P'),
                )
                print(f' Created AbsorptionRate {NewAbsorptionRate}')
            except Exception as e:
                print(f' Was cause Exseption {e}')

    def CreateChemicalCompositionEntity(self, Data: dict):
        with db_session:
            try:
                NewChemicalComposition = self.db.ChemicalComposition(
                    MaterialName=Data.get('MaterialName'),
                    C=Data.get('C'),
                    Mn=Data.get('Mn'),
                    Si=Data.get('Si'),
                    Cr=Data.get('Cr'),
                    Ti=Data.get('Ti'),
                    V=Data.get('V'),
                    Mo=Data.get('Mo'),
                    B=Data.get('B'),
                    Nb=Data.get('Nb'),
                    Ni=Data.get('Ni'),
                    Cu=Data.get('Cu'),
                    Al=Data.get('Al'),
                    S=Data.get('S'),
                    Fe=Data.get('Fe'),
                    Ca=Data.get('Ca'),
                    P=Data.get('P'),
                )
                print(f' Created ChemicalComposition {NewChemicalComposition}')
            except Exception as e:
                print(f' Was cause Exseption {e}')

    def CreateFuseEntity(self, Data: dict):
        with db_session:
            try:
                NewFuse = self.db.Fuse(
                    Tcn=Data.get('Tcn'),
                    FuseName=Data.get('FuseName'),
                    TempVd=Data.get('TempVd'),
                    Temp_ccm1=Data.get('Temp_ccm1'),
                    Temp_ccm2=Data.get('Temp_ccm2'),
                    C=Data.get('C'),
                    Si=Data.get('Si'),
                    Mn=Data.get('Mn'),
                    S=Data.get('S'),
                    Al=Data.get('Al'),
                    Cr=Data.get('Cr'),
                    Mo=Data.get('Mo'),
                    Ni=Data.get('Ni'),
                    Cu=Data.get('Cu'),
                    V=Data.get('V'),
                    Nb=Data.get('Nb'),
                    Ti=Data.get('Ti'),
                    B=Data.get('B'),
                    Ca=Data.get('Ca'),
                    Cpr=Data.get('Cpr'),
                )

                print(f' Created Fuse {NewFuse}')
            except Exception as e:
                print(f' Was cause Exseption {e}')

    def CreateCoredWireEntity(self, Data: dict):
        with db_session:
            try:
                NewCoreWire = self.db.CoredWire(
                    CWName=Data.get('CWName'),
                    provider=Data.get('provider'),
                    CorWire=Data.get('CorWire'),
                    weight=Data.get('weight')
                )

                print(f' Created CoreWire {NewCoreWire}')
            except Exception as e:
                print(f' Was cause Exseption {e}')


class DeleteServices(CreateServices):
    pass


class UpdateServices(CreateServices):

    def __init(self, Data: dict):
        self.Data = Data

    def UpdateService(self):
        with db_session:


            try:

                NameDbList = ['AbsorptionRate', 'ChemicalComposition', 'CoredWire', 'Fuse'].pop(self.Data.get('NameDb'))

                NewRequest = self.db.NameDbList.get(self.Data.get('Tcn'))

                NewRequest[NewRequest.ID] = set(**self.Data)

            except Exception as e:
                pass
