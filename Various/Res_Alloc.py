# VDLS 12/02/19 - Resource Allocation Algorithm

# Rules to split work over capacity constraints.

# 1 .- Same shift and PM.
# 2 .- Same shift, different PM.
# 3 .- Same PM, different PM.
# 4 .- Different shift and PM.

# Libraries import

import sys
import numpy as np
import pandas as pd

# Read Files

user_file_loc = r'C:\Users\liceaga\Desktop\Resource_Allocation\user_skill_matrix.csv'
user_df = pd.read_csv(user_file_loc)
ws_file_loc = r'C:\Users\liceaga\Desktop\Resource_Allocation\ws_skill_matrix.csv'
ws_df = pd.read_csv(ws_file_loc)

# Define matrices to multiply

rs = user_df.iloc[:,3:198]
ws = ws_df.iloc[:-1,1:-1]

# Define weight vector, TODO: add column to ws_skill_matrix to use as weight vector /Done 

wv = ws_df.iloc[:-1,-1]

# Multiply WS matrix by wv

ws_w = ws.mul(wv, axis = 0)

# Calculate Allocation Matrix #TODO: Reindex am by id_emp /Done
# np.dot(rs,ws_w) dot is easier to carry out as np but then we would need to convert back to df

am = rs.dot(ws_w.set_index(ws_df.iloc[:195,0])).set_index(user_df.iloc[:215,0])

print(am)

#TODO: Calculate # of resources to assign to each WS
# Add as a bottom row at ws_df? ws_df.loc[199] = [Generated vector with corresponding values]

#TODO: WS priority list to assign resources /Done, added as last row in ws_df
#TODO: Loop through WS priority list allocating resources by sorting corresponding am column
#TODO: Pick top resources needed from sorted column to match capacity needs, assing to WS
#TODO: Remove allocated resources by id_emp from am matrix