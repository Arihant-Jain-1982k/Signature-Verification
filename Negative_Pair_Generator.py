import random
import pandas as pd
source = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
author = list(range(55))

#Original to original mapping
dataset = pd.DataFrame(data = None)
for i in range(55):
    authors = [x for x in author if x != i]
    l1 = random.sample(source, 10)
    l2 = random.sample(source, 10)
    l3 = random.sample(authors, 10)
    l1 = [float(format((item/100 + i + 1), '.2f')) for item in l1]
    l2 = [float(format((l2[item]/100 + l3[item] + 1), '.2f')) for item in range(10)]
    for j in range(10):
        for k in range(10):
            dataset = dataset.append([[l1[j], l2[k], 0]], ignore_index = True)
    print(i)
dataset = dataset.rename(columns={0:'Img1', 1:'Img2', 2:'Label'})

dataset.to_csv("Negative_Pairs_Originals.csv")

#Originals to forgeries mapping
dataset = pd.DataFrame(data = None)
for i in range(55):
    l1 = random.sample(source, 10)
    l2 = random.sample(source, 10)
    l1 = [float(format((item/100 + i + 1), '.2f')) for item in l1]
    l2 = [float(format((item/100 + i + 1), '.2f')) for item in l2]
    for j in range(10):
        for k in range(10):
            dataset = dataset.append([[l1[j], l2[k], 0]], ignore_index = True)
    print(i)
dataset = dataset.rename(columns={0:'Img1', 1:'Img2', 2:'Label'})

dataset.to_csv("Negative_Pairs_Forgeries.csv")

#Originals to both mapping (80% originals, 20% Forgeries) 
dataset = pd.DataFrame(data = None)
for i in range(55):
    authors = [x for x in author if x != i]
    l1 = random.sample(source, 10)
    l2 = random.sample(source, 10)
    l3 = random.sample(authors, 8)
    l3 = l3 + [i,i]
    l1 = [float(format((item/100 + i + 1), '.2f')) for item in l1]
    l2 = [float(format((l2[item]/100 + l3[item] + 1), '.2f')) for item in range(10)]
    for j in range(10):
        for k in range(10):
            dataset = dataset.append([[l1[j], l2[k], 0]], ignore_index = True)
    print(i)
dataset = dataset.rename(columns={0:'Img1', 1:'Img2', 2:'Label'})

dataset.to_csv("Negative_Pairs_8020.csv")

#Originals to both mapping (50% originals, 50% Forgeries) 
dataset = pd.DataFrame(data = None)
for i in range(55):
    authors = [x for x in author if x != i]
    l1 = random.sample(source, 10)
    l2 = random.sample(source, 10)
    l3 = random.sample(authors, 5)
    l3 = l3 + [i,i,i,i,i]
    l1 = [float(format((item/100 + i + 1), '.2f')) for item in l1]
    l2 = [float(format((l2[item]/100 + l3[item] + 1), '.2f')) for item in range(10)]
    for j in range(10):
        for k in range(10):
            dataset = dataset.append([[l1[j], l2[k], 0]], ignore_index = True)
    print(i)
dataset = dataset.rename(columns={0:'Img1', 1:'Img2', 2:'Label'})

dataset.to_csv("Negative_Pairs_5050.csv")