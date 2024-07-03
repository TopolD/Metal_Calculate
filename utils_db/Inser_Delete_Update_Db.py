from utils_db.services import AbsorptionRateEntity


class WorkWithEntityInstances:

    def __init__(self):
        self.Absorp = AbsorptionRateEntity()

    def MathchData(self, Data: dict):
        try:
            match Data.get("NameDb"):
                case 'AbsorptionRate':
                    return self.Absorp()
                case 'ChemicalComposition':
                    return self.Se.CreateChemicalCompositionEntity(Data)
                case 'CoredWire':
                    return self.Se.CreateCoredWireEntity(Data)
                case 'Fuse':
                    return self.Se.CreateFuseEntity(Data)
                case _:
                    return False
        except Exception as e:
            print(f'Was  caused an exception {e}')

    def CreatingEntity(self):
        try:
            self.MathchData()
        except Exception as e:
            print(f' Was cause Exseption {e}')

    def DeleteEntity(self):
        pass

    def UpdateEntity(self):
        try:
