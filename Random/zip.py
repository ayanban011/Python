a = [10,20,20,10,10,30,50,10,20]
from itertools import groupby
print([len(list(group)) for key, group in groupby(a)])
