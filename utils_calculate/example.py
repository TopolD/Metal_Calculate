from formuls_for_calculate import CalculateRemainderMaterial, DataHolder

Tcn = ('222'
       '')
Data = {
    'W': 160.0,
    'samples': {
        'C': 0,
        'Si': 0,
        'Mn': 0,

    },
    'corewire':{
        'C':0,
        'Al':0.007,
        'Ti':0,

    },
    'material': {
        'C': 'GKA',
        'Si': 'FeSi75',
        'Mn': 'SiMn17',

    }

}
DataHolder.set_data(Tcn, Data)
result = CalculateRemainderMaterial()
example_result = result._calculate_materials_c()
print(example_result)
