import sys
import numpy as np
import pandas as pd

rs_matrix = pd.read_csv(r'C:\Users\liceaga\Desktop\Resource_Allocation\user_skill_matrix.csv', sep=",")
ws_matrix = pd.read_csv(r'C:\Users\liceaga\Desktop\Resource_Allocation\ws_skill_matrix.csv', sep=",")
rs = rs_matrix.iloc[:,3:198]
ws = ws_matrix.iloc[0:-1,:28]

result = rs.dot(ws.set_index('Skills'))
print(result)