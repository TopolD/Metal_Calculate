from utils_db.services import CreateServices, DeleteServices, UpdateServices


class WorkWithEntityInstances:

    def __init__(self):
        self.csv = CreateServices()
        self.dsv = DeleteServices()
        self.usv = UpdateServices()

    def MathchData(self, NameDb: str, DictData: dict):
        try:
            match NameDb:
                case 'AbsorptionRate':
                    return self.csv.CreateAbsorptionRateEntity(DictData)
                case 'ChemicalComposition':
                    return self.csv.CreateChemicalCompositionEntity(DictData)
                case 'CoredWire':
                    return self.csv.CreateCoredWireEntity(DictData)
                case 'Fuse':
                    return self.csv.CreateFuseEntity(DictData)
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
