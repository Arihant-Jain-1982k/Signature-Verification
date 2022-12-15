import random
import pandas as pd
source = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
dataset = pd.DataFrame(data = None)
for i in range(55):
    l1 = random.sample(source, 10)
    new_source = [item for item in source if item not in l1]
    l2 = random.sample(new_source, 10)
    l1 = [float(format((item/100 + i + 1), '.2f')) for item in l1]
    l2 = [float(format((item/100 + i + 1), '.2f')) for item in l2]
    for j in range(10):
        for k in range(10):
            dataset = dataset.append([[l1[j], l2[k], 1]], ignore_index = True)
    print(i)
    
dataset = dataset.rename(columns={0:'Img1', 1:'Img2', 2:'Label'})
dataset.to_csv("Positive_Pairs.csv")