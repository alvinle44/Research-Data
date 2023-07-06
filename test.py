import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dict1 = {'A': [1, 2, 3], 'B':[2, 5, 6],}
f = ('k', 'm', 'z')
df = pd.DataFrame.from_dict(dict1, orient='index', columns=f)
print(df)