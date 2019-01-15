# VDLS - 09/01/19 - Pandas Documentation Lesson 1

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib

# Enable inline plotting
%matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

# Create Data / Initial set of baby names and birth rates.
names = ['Bob','Jessica','Mary','John','Mel']
births = [968,155,77,578,973]
# Merge with zip
BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet, columns = ['Names','Births'])
df.to_csv('births1880.csv',index=False,header=False)