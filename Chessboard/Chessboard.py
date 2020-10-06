import numpy as np
import pandas as pd
from scipy.spatial import distance 
import random
 
data = pd.read_csv("Point_Data.csv")


lp = []
for i in data.itertuples():
    lp.append((round(i.x,3), round(i.y,3)))

random = random.choices(lp, k= 200)
dis = [] 
for i in range(len(lp)):
    x1, y1 = lp[i]
    p = np.array([x1, y1])
    row = []
    for j in range (len(lp)):
        x2, y2 = lp[j]
        q = np.array([x2, y2])
        dist = distance.chebyshev(p,q)
        row.append(dist)
    dis.append(row)
   
dfs = pd.DataFrame(dis)
dfs.to_csv("result_chessboard_1000.csv", index= False)
