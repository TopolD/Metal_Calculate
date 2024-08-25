from pony.orm import db_session
from utils_db.Db_models import ConnDb


class Instance(ConnDb):

    def GetInstance(self, Data: dict, model_name, field_name, field_value):
        try:
            with db_session:
                model = getattr(self.db, model_name)
                return model.get(**{field_name: field_value})
        except Exception as e:
            print(f' Error {e}')
        finally:
            db_session.close()


class AbsorptionRateEntity(Instance):

    def __init__(self):
        super().__init__()

    def CreateAbsorptionRateEntity(self, Data: dict):
        try:
            with db_session:

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
            print(f' Error create entity: {e}')

    def DeleteEntityAbsor(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'AbsorptionRate', 'AbrName', Data.get('AbrName'))
                if instance:
                    instance.delete()
                    print(f'Entity with AbrName {instance} was deleted')
                else:
                    print('Entity not found')
        except Exception as e:
            print(f"Error deleted entity: {e}")

    def UpdateEntityAbsor(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'AbsorptionRate', 'AbrName', Data.get('AbrName'))
                if instance:
                    instance.set(**Data)
                    print(f'Entity with AbrName {instance} was deleted')
                else:
                    print('Entity not update')
        except Exception as e:
            print(f"Error updating entity: {e}")


class ChemicalCompositionEntity(Instance):
    def CreateChemicalCompositionEntity(self, Data: dict):
        try:
            with db_session:

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
            print(f' Error create entity: {e}')

    def DeleteEntityChemical(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'ChemicalComposition', 'MaterialName', Data.get('MaterialName'))
                if instance:
                    instance.delete()
                    print(f'Entity with MaterialName {instance} was deleted')
                else:
                    print('Entity not found')
        except Exception as e:
            print(f"Error deleted entity: {e}")

    def UpdateEntityChemical(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'ChemicalComposition', 'MaterialName', Data.get('MaterialName'))
                if instance:
                    instance.set(**Data)
                    print(f'Entity with MaterialName {instance} was deleted')
                else:
                    print('Entity not update')
        except Exception as e:
            print(f"Error updating entity: {e}")


class FuseEntity(Instance):
    def CreateFuseEntity(self, Data: dict):
        try:
            with db_session:

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
                    Cpr=Data.get('Cpr')
                )
                print(f' Created Fuse {NewFuse}')
        except Exception as e:
            print(f' Error create entity: {e}')

    def DeleteEntityChemical(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'Fuse', 'FuseName', Data.get('FuseName'))
                if instance:
                    instance.delete()
                    print(f'Entity with FuseName {instance} was deleted')
                else:
                    print('Entity not found')
        except Exception as e:
            print(f"Error deleted entity: {e}")

    def UpdateEntityChemical(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'Fuse', 'FuseName', Data.get('FuseName'))
                if instance:
                    instance.set(**Data)
                    print(f'Entity with Fuse {instance} was deleted')
                else:
                    print('Entity not update')
        except Exception as e:
            print(f"Error updating entity: {e}")


#
class CoredWireEntity(Instance):
    def CreateCoredWireEntity(self, Data: dict):
        try:
            with db_session:

                NewCoreWire = self.db.CoredWire(
                    CWName=Data.get('CWName'),
                    provider=Data.get('provider'),
                    CorWire=Data.get('CorWire'),
                    weight=Data.get('weight'),

                )
                print(f' Created CoreWire {NewCoreWire}')
        except Exception as e:
            print(f' Error create entity: {e}')

    def DeleteEntityCoredWire(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'CoredWire', 'CWName', Data.get('CWName'))
                if instance:
                    instance.delete()
                    print(f'Entity with CWName {instance} was deleted')
                else:
                    print('Entity not found')
        except Exception as e:
            print(f"Error deleted entity: {e}")

    def UpdateEntityCoredWire(self, Data: dict):
        try:
            with db_session:
                instance = self.GetInstance(Data, 'CoredWire', 'CWName', Data.get('CWName'))
                if instance:
                    instance.set(**Data)
                    print(f'Entity with CWName {instance} was deleted')
                else:
                    print('Entity not update')
        except Exception as e:
            print(f"Error updating entity: {e}")
