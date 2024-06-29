from Inser_Delete_Update_Db import *

DictData = {
    'Tcn': '1',
    'FuseName': '1',
    'TempVd': '1',
    'Temp_ccm1': '1',
    'Temp_ccm2': '1',
    'C': '1',
    'Si': '1',
    'Mn': '1',
    'S': '0.01',
    'Al': '0.02',
    'Cr': '0.03',
    'Mo': '0.04',
    'Ni': '0.05',
    'Cu': '0.06',
    'V': '0.07',
    'Nb': '0.08',
    'Ti': '0.09',
    'B': '0.10',
    'Ca': '0.11',
    'Cpr': '0.12',
}

example = WorkWithEntityInstances()

result = example.CreatingEntity('Fuse', DictData)
