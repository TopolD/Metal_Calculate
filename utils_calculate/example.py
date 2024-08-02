from Formuls_example import GetDataCalculate

Tcn = ('159'
       '')
Data = {
    'W': 170.0,
    'samples': {
        'C': 0.49,
        'Si': 0.2,
        'Mn': 0.3,
        'Cr':0.15
    },
    'material': {
        'C': 'GKA',
        'Si': 'FeSi65',
        'Mn': 'SiMn17',
        'Cr': 'FeCr800'
    }

}

example = GetDataCalculate(Tcn, Data)
result = example.material()

print(result)