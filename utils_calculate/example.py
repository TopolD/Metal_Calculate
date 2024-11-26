from formuls_for_calculate import calculate_material, DataHolder, get_data_calculate_with_db, \
    calculate_core_wire

Tcn = ('313   ')
Data = {
    'W': 160.0,
    'samples': {
       'C': '0',
       'Si': '0.1',
       'Mn': '0.34 ',


    },
    'corewire':{'Al':'0',
                'Ti':'0',
                'Ca':'0.05'},
    'material': {
        'C': 'GKA',
        'Si': 'FeSi65',
        'Mn': 'SiMn17',
        'Ti':'FeTi70'


    },
    'temp':'1569'

}
DataHolder.set_data(Tcn, Data)
result = calculate_core_wire()
example_result = result._calculate_core_wire_ca()
print(example_result)

