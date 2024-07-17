from Formuls import GetDataCalculate

Tcn = '26'
Data = {
    'W': 170,
    'C': 0.03,
    'NameC': 'GKA',
    'Si': 0.20,
    'NameSi': 'FeSi65',
    'Mn': 0.3,
    'NameMn': 'SiMn17'
}

example = GetDataCalculate(Tcn)
result = example.GetBaseDataMaterial(Data)

print(result)
