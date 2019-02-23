# VDLS - 11/21/2018 - K Nearest Neighbors Algorithm 

import numpy as np
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
import pandas as pd
import random

style.use('fivethirtyeight')

# Öne line För Lööp Bröther
# [[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K has a wrong value!')
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_dist = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_dist, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(vote).most_common(1)[0][0]

    return vote_result, confidence
df = pd.read_csv(r'C:\Users\liceaga\Desktop\Python_Work\Sentdex\Data_BC.txt')
df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)
# Convert data set into specific data type
full_data = df.astype(float).values.tolist()
# Shuffle sata randomly
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote , confidence = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1
print('Accuracy', correct/total)