# VDLS 12/02/19 - Resource Allocation Algorithm

# Rules to split work over capacity constraints.

# 1 .- Same shift and PM.
# 2 .- Same shift, different PM.
# 3 .- Same PM, different PM.
# 4 .- Different shift and PM.

# Libraries import

import numpy as np
import pandas as pd

# Read Files

user_file_loc = r'C:\Users\liceaga\Desktop\Resource_Allocation\user_skill_matrix.csv'
user_df = pd.read_csv(user_file_loc)
ws_file_loc = r'C:\Users\liceaga\Desktop\Resource_Allocation\ws_skill_matrix.csv'
ws_df = pd.read_csv(ws_file_loc)

# Define matrices to multiply

rs = user_df.iloc[:,3:198]
ws = ws_df.iloc[0:-1,:28]

# Define weight vector, TODO: add column to ws_skill_matrix to use as weight vector /Done 

wv = ws_df.weight[:195]

# Multiply WS matrix by wieght vector

ws.apply(lambda x: np.asarray(x) * np.asarray(wv))

print(ws)

result = rs.dot(ws.set_index('Skills'))

print(result)

