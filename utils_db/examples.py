from services import *

DictData = {
    'AbrName': '1',
    'C': '1',
    'Mn': '1',
    'Si': '1',
    'Cr': '1',
    'Ti': '1',
    'V': '1',
    'Mo': '1',
    'B': '0.01',
    'Nb': '0.02',
    'Ni': '0.03',
    'Cu': '0.04',
    'Al': '0.05',
    'S': '0.06',
    'Fe': '0.07',
    'Ca': '0.08',
    'P': '0.09',
}

example = AbsorptionRateEntity()

result = example.DeleteEntityAbsor(DictData)
