import numpy as np
import pandas as pd
from scipy.spatial import distance
import random
df = pd.read_csv("Point_Data.csv")


lp = []
for i in df.itertuples():
    lp.append((round(i.x,3), round(i.y,3)))
random = random.choices(lp, k = 200) 

dis = []
for i in range(len(lp)):
    x1, y1 = lp[i]
    p = np.array([x1, y1])
    row = []
    for j in range(len(lp)):
        x2, y2 = lp[j]
        q = np.array([x2, y2])
        dist = distance.hamming(p,q)
        row.append(round(dist, 3))
    dis.append(row)
    
dfs = pd.DataFrame(dis)
dfs.to_csv('result_1000hamming.csv', index = False)