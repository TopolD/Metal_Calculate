from Formuls import GetDataCalculate
from pony.orm import *




Tcn='181'



example = GetDataCalculate(Tcn)
result = example.GetDataFuse()



print(result)