import numpy as np
import pandas as pd
from numpy.linalg import norm
import random
data = pd.read_csv("Point_Data.csv")

lp = []
for i in data.itertuples():
    lp.append((round(i.x,3), round(i.y,3)))
    
random = random.choices(lp, k = 200)

dis = [] 
for i in range(len(lp)):
    x1, y1 = lp[i]
    p = np.array([x1, y1])
    row = []
    for j in range (len(lp)):
        x2, y2 = lp[j]
        q = np.array([x2, y2])
        dist = norm(p - q)
        row.append(round(dist,3))
    dis.append(row)
    

dfs = pd.DataFrame(dis)
dfs.to_csv("result_1000_euclid.csv", index= False)
