from utils_db.services import CreateServices, DeleteServices, UpdateServices


class WorkWithEntityInstances:

    def __init__(self, NameDb):
        self.csv = CreateServices()
        self.dsv = DeleteServices()
        self.usv = UpdateServices()

    def MathchData(self, Data: dict):
        try:
            match Data.get("NameDb"):
                case 'AbsorptionRate':
                    return self.csv.CreateAbsorptionRateEntity(Data)
                case 'ChemicalComposition':
                    return self.csv.CreateChemicalCompositionEntity(Data)
                case 'CoredWire':
                    return self.csv.CreateCoredWireEntity(Data)
                case 'Fuse':
                    return self.csv.CreateFuseEntity(Data)
                case _:
                    return False
        except Exception as e:
            print(f'Was  caused an exception {e}')

    def CreatingEntity(self, DictData: dict):
        try:
            self.MathchData(DictData)
        except Exception as e:
            print(f' Was cause Exseption {e}')

    def DeleteEntity(self, NameCol):
        pass

    def UpdateEntity(self, NameCol, Col, Data: dict):
        pass
