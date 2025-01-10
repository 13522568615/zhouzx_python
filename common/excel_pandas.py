import pandas as pd
import os
import openpyxl

path = os.path.dirname(os.path.dirname(__file__))
data = os.path.join(path, 'selenium代码/codemoss_data.xlsx')
print("")
df = pd.read_excel(data, index_col=None, header=None)
for row in df.itertuples(index=False):
    print(row[0], row[1], row[2], row[3], row[4])