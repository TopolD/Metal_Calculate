from Formuls import GetDataCalculate



Tcn = '159'
Data = {
    'W': 170,
    'C': 0.1,
    'NameC': 'GKA',
    'Si': 0.2,
    'NameSi': 'FeSi65',
    'Mn': 0.3,
    'NameMn': 'SiMn17',
    'Cr':0,
    'NameCr':'FeCr800'
}

example = GetDataCalculate(Tcn)
result = example.GetBaseDataMaterial(Data)

print(result)