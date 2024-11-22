from formuls_for_calculate import calculate_material, DataHolder, get_data_calculate_with_db, \
    calculate_core_wire

Tcn = ('59')
Data = {
    'W': 160.0,
    'samples': {
       'C': '0',
       'Si': '0.1',
       'Mn': '0.34 ',
        'Cr':'0'


    },
    'corewire':{'Al':'0',
                'Ti':'0'},
    'material': {
        'C': 'GKA',
        'Si': 'FeSi65',
        'Mn': 'SiMn17',
        'Cr':'FeCr800',
        'Ti':'FeTi70'

    }

}
DataHolder.set_data(Tcn, Data)
result = calculate_material()
example_result = result._calculate_materials_si()
print(example_result)

