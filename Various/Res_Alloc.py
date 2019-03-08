# VDLS 08/3/19 - Resource Allocation Algorithm - V0.5

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
ws = ws_df.iloc[:195,1:-1]

wv = ws_df.iloc[:195,-1]        # Define weight vector.
ws_w = ws.mul(wv, axis = 0)     # Multiply WS matrix by wv.

# Calculate Allocation Matrix, Reindex am by id_emp.
# np.dot(rs,ws_w) dot is easier to carry out as np but then we would need to convert back to df
am = rs.dot(ws_w.set_index(ws_df.iloc[:195,0])).set_index(user_df.iloc[:215,0]) 

rn = ws_df[ws_df.index.isin([190, 195, 196])]   # Create intermediate table to make calculations.
rn = rn.drop(['weight'], axis=1).T              # Removing unnecesary row and transposing to make column operations easier.

new_header = rn.iloc[0]         # grab the first row for the header
rn = rn[1:]                     # take the data less the header row
rn.columns = new_header         # set the header row as the df header

# Add column with number of resources needed (R_N).

rn['R_N'] = np.where(rn['Day Shift'] == 1, rn['Capacity']/540, rn['Capacity']/465)

rn['R_N'] = np.where(rn['R_N'] < 1, 1, rn['R_N'].astype(int)) # if R_N < 1 then R_N = 1 else R_N = int(R_N)

# Edit R_N float format. LoL, Not needed but i wanted to know how to do it.
# rn['R_N'] = rn['R_N'].map('{:,.2f}'.format)

rn = rn.sort_values('Priority')     # Sort R_N table by WS priority.

# Main Allocation loop.
#TODO: Change FOR loop to WHILE + capacity cond check? 

c = 0                               # Counter for index matching between tables
out_alloc = pd.DataFrame()          # Empty DF.

for i in rn.index.values:           # Loop to allocate resources and update matrices.
    am = am.sort_values(i)          # Sort and update Alloc_matrix.
    selected = am.index.values[:int(rn.iloc[c][3])]                     # Pick top users for WS, line separated for readability.
    sel_col = pd.Series(data=selected, index=None, dtype=str, name=i)   # Transform Data into a Column with WS name as header.
    out_alloc[i] =  sel_col         # Allocated Resources table.
    am = am.drop(selected)          # Reduce Alloc_matrix each iteration.
    c += 1

print(out_alloc)                    #TODO: Replace id_emp by emp_name for easier viz.

rn['Allocated'] = np.where(rn['Day Shift'] == 1, rn['R_N']*540, rn['R_N']*465)  # Create allocated hours column.
rn['Residue'] = (rn['Capacity'] - rn['Allocated']).abs()                        # Calculate residual alloc hours.

print(rn)   # Final resources needed table.
print(100*rn.Allocated.sum()/rn.Capacity.sum()) # Total Allocated %.

# TODO: Improve allocation method to increase total allocation %.

# TODO(Chony): Feedback pls.

# Write any df to .CSV
#am_output = r'C:\Users\liceaga\Desktop\Resource_Allocation\am_matrix.csv'
#am.to_csv(am_output)
#TODO: Transform problem and solve as LP/IP?