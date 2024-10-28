from formuls_for_calculate import calculate_remainder_material, DataHolder, get_data_calculate_with_db

Tcn = ('164'
       '')
Data = {
    'W': 160.0,
    'samples': {
       'C': '0',
       'Si': '0',
       'Mn': '0',
       'Cr':'0'

    },
    'corewire':{},
    'material': {
       'C': 'GKA',
       'Si': 'FeSi75',
       'Mn': 'SiMn17',
       'Cr':'FeCr800'

    }

}
DataHolder.set_data(Tcn, Data)
result = calculate_remainder_material()
example_result = result._calculate_materials_c()
print(example_result)

