from pony.orm import *
from utils_db.Db_models import ConnDb
from utils_db.services import Services


class WorkWithEntityInstances:

    def __init__(self):
        self.db = ConnDb()
        self.sv = Services()

    def MathchData(self, NameDb: str, DictData: dict):
        try:
            match NameDb:
                case 'AbsorptionRate':
                    return self.sv.CreateAbsorptionRateEntity(DictData)
                case 'ChemicalComposition':
                    return self.sv.CreateChemicalCompositionEntity(DictData)
                case 'CoredWire':
                    return self.sv.CreateCoredWireEntity(DictData)
                case 'Fuse':
                    return self.sv.CreateFuseEntity(DictData)
                case _:
                    return False
        except Exception as e:
            print(f'Was  caused an exception {e}')

    def CreatingEntity(self, NameDb: str, DictData: dict):
        try:
            self.MathchData(NameDb, DictData)
        except:
            pass  # доделать исключение!

    def DeleteEntity(self, NameCol):
        pass

    def UpdateEntity(self, NameCol, Col, Data):
        pass
