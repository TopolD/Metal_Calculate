from Formuls import GetDataCalculate

Tcn = '26'
Data = {
    'W':160,
    'C':0.03,
    'NameC':'GKA',
    'Si': 0.20,
    'NameSi':'Fesi65'
}

example = GetDataCalculate(Tcn)
result = example.GetDataMaterial(Data)

print(result)
