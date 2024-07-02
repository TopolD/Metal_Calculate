from pony.orm import *
from utils_db.Db_models import ConnDb


class GetDataCalculate:

    def __init__(self, Tcn):
        self.db = ConnDb()
        self.Tcn = Tcn

        self.GetData()

    @staticmethod
    def is_nan(value):
        try:
            import math
            return math.isnan(float(value))
        except (ValueError, TypeError):
            return False

    def GetData(self):
        try:
            instance = self.db.Fuse.get(Tcn=self.Tcn)
            Non_none_values = {}
            if instance:
                for attr_name, attr_value in instance.to_dict().items():
                    if not self.is_nan(attr_value) and attr_value is not None:
                        Non_none_values[attr_name] = attr_value
            return Non_none_values
        except MultipleRowsFound as Error:
            print(f'Multiple rows {Error}')
        except ObjectNotFound as Error:
            print(f' Object not found: {Error}')
        except MultipleObjectsFoundError as Error:
            print(f' several objects detected: {Error}')
