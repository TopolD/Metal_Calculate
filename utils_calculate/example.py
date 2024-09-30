from Formuls_example import Calculate, DataHolder

Tcn = ('222'
       '')
Data = {
    'W': 160.0,
    'samples': {
        'C': 0,
        'Si': 0,
        'Mn': 0,

    },
    'material': {
        'C': 'GKA',
        'Si': 'FeSi75',
        'Mn': 'SiMn17',

    }

}
DataHolder.set_data(Tcn, Data)
result = Calculate()
example_result = result._calculate_materials_si()
print(example_result)
