# VDLS 12/02/19 - Resource Allocation Algorithm

# Rules to split work over capacity constraints.

# 1 .- Same shift and PM.
# 2 .- Same shift, different PM.
# 3 .- Same PM, different PM.
# 4 .- Different shift and PM.

## Libraries import

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
ws = ws_df.iloc[:195,1:-1]

# Define weight vector, TODO: add column to ws_skill_matrix to use as weight vector /Done 

wv = ws_df.iloc[:195,-1]

# Multiply WS matrix by wv

ws_w = ws.mul(wv, axis = 0)

# Calculate Allocation Matrix #TODO: Reindex am by id_emp /Done
# np.dot(rs,ws_w) dot is easier to carry out as np but then we would need to convert back to df

am = rs.dot(ws_w.set_index(ws_df.iloc[:195,0])).set_index(user_df.iloc[:215,0])

# Calculate Resources Needed for each WS (rn).
# Create intermediate table to make calculations.

rn = ws_df[ws_df.index.isin([190, 195, 196])]

# Removing unnecesary row and transposing to make column operations easier.

rn = rn.drop(['weight'], axis=1).T

new_header = rn.iloc[0] #grab the first row for the header
rn = rn[1:] #take the data less the header row
rn.columns = new_header #set the header row as the df header

# Add column with number of resources needed (R_N).

rn['R_N'] = np.where(rn['Day Shift'] == 1, rn['Capacity']/540, rn['Capacity']/465)

# Edit R_N float format. LoL, Not needed but i wanted to know how to do it.
# rn['R_N'] = rn['R_N'].map('{:,.2f}'.format)

# Sort R_N table by WS priority.

rn.sort_values('Priority')

# Write Allocation Matrix to .CSV

am_output = r'C:\Users\liceaga\Desktop\Resource_Allocation\am_matrix.csv'
am.to_csv(am_output)

# Loop to allocate resources and update matrices.
# Loop to allocate resources and update matrices.
out_alloc= pd.DataFrame()
c = 0 # counter for index matching between tables
for i in rn.index.values:
    am.sort_values(i)
    selected = am.index.values[:int(rn.iloc[c][3])]
    sel_col = pd.Series(data=selected, index=None, dtype=str)
    z = pd.concat([out_alloc, sel_col], ignore_index=False, axis=1)
    am = am.drop(selected)
    print(z)
    c += 1
    