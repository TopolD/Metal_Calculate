from formuls_for_calculate import calculate_remainder_material, DataHolder, get_data_calculate_with_db

Tcn = ('999'
       '')
# Data = {
#     'W': 160.0,
#     'samples': {
#         'C': 0,
#         'Si': 0,
#         'Mn': 0,
#
#     },
#     'corewire':{
#         'C':0,
#         'Al':0.007,
#         'Ti':0,
#
#     },
#     'material': {
#         'C': 'GKA',
#         'Si': 'FeSi75',
#         'Mn': 'SiMn17',
#
#     }
#
# }
DataHolder.set_data(Tcn, None)
# result = calculate_remainder_material()
# example_result = result._calculate_materials_c()
# print(example_result)


result = get_data_calculate_with_db()
example_result = result.get_data_target_for_fuse()
print(example_result)