import pandas as pd
import numpy as np
from PIL import Image


data1 = pd.read_csv("Positive_Pairs.csv", index_col=0)
data2 = pd.read_csv("Negative_Pairs_Originals.csv", index_col=0)
data3 = data1.append(data2, ignore_index=True)
data3 = data3.sample(frac=1, random_state=0)
data3.reset_index(inplace=True, drop=True)
y = list(data3.Label)
x = np.zeros((1,2,100,100)).astype(int)

for j in range(44):
    x_batch = np.zeros((1,2,100,100)).astype(int)
    for i in range(250):
        author1 = str(data3.Img1[i].astype(int))
        image1 = str(int(((data3.Img1[i] - data3.Img1[i].astype(int))*100).round()))
        
        author2 = str(data3.Img2[i].astype(int))
        image2 = str(int(((data3.Img2[i] - data3.Img2[i].astype(int))*100).round()))
        
        img1 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author1 + "_" + image1 + ".png")), (1,1,100,100)).astype(int)
        img2 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        
        pair = np.append(img1, img2, axis=1)
        x_batch = np.append(x_batch, pair, axis = 0)
        print((250*j) + i)
    x_batch = np.delete(x_batch, 0, axis=0)
    x = np.append(x, x_batch, axis = 0)
    print("----------END OF BATCH----------")

x = np.delete(x, 0, axis=0)

np.save("Dataset/X_Originals", x)
np.save("Dataset/Y_Originals", y)


data1 = pd.read_csv("Positive_Pairs.csv", index_col=0)
data2 = pd.read_csv("Negative_Pairs_Forgeries.csv", index_col=0)
data3 = data1.append(data2, ignore_index=True)
data3 = data3.sample(frac=1, random_state=0)
data3.reset_index(inplace=True, drop=True)
y = list(data3.Label)
x = np.zeros((1,2,100,100)).astype(int)

for j in range(44):
    x_batch = np.zeros((1,2,100,100)).astype(int)
    for i in range(250):
        author1 = str(data3.Img1[i].astype(int))
        image1 = str(int(((data3.Img1[i] - data3.Img1[i].astype(int))*100).round()))
        
        author2 = str(data3.Img2[i].astype(int))
        image2 = str(int(((data3.Img2[i] - data3.Img2[i].astype(int))*100).round()))
        
        img1 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author1 + "_" + image1 + ".png")), (1,1,100,100)).astype(int)
        img2 = np.reshape(np.array(Image.open("Dataset/full_forg/forgeries_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        
        pair = np.append(img1, img2, axis=1)
        x_batch = np.append(x_batch, pair, axis = 0)
        print((250*j) + i)
    x_batch = np.delete(x_batch, 0, axis=0)
    x = np.append(x, x_batch, axis = 0)
    print("----------END OF BATCH----------")

x = np.delete(x, 0, axis=0)

np.save("Dataset/X_Forgeries", x)
np.save("Dataset/Y_Forgeries", y)


data1 = pd.read_csv("Positive_Pairs.csv", index_col=0)
data2 = pd.read_csv("Negative_Pairs_5050.csv", index_col=0)
data3 = data1.append(data2, ignore_index=True)
data3 = data3.sample(frac=1, random_state=0)
data3.reset_index(inplace=True, drop=True)
y = list(data3.Label)
x = np.zeros((1,2,100,100)).astype(int)

for j in range(44):
    x_batch = np.zeros((1,2,100,100)).astype(int)
    for i in range(250):
        author1 = str(data3.Img1[i].astype(int))
        image1 = str(int(((data3.Img1[i] - data3.Img1[i].astype(int))*100).round()))
        
        author2 = str(data3.Img2[i].astype(int))
        image2 = str(int(((data3.Img2[i] - data3.Img2[i].astype(int))*100).round()))
        
        img1 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author1 + "_" + image1 + ".png")), (1,1,100,100)).astype(int)
        if author1==author2:
            if y[(j*250) + i] == 0:
                img2 = np.reshape(np.array(Image.open("Dataset/full_forg/forgeries_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
            else:
                img2 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        else:
            img2 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        
        pair = np.append(img1, img2, axis=1)
        x_batch = np.append(x_batch, pair, axis = 0)
        print((250*j) + i)
    x_batch = np.delete(x_batch, 0, axis=0)
    x = np.append(x, x_batch, axis = 0)
    print("----------END OF BATCH----------")

x = np.delete(x, 0, axis=0)

np.save("Dataset/X_5050", x)
np.save("Dataset/Y_5050", y)

data1 = pd.read_csv("Positive_Pairs.csv", index_col=0)
data2 = pd.read_csv("Negative_Pairs_8020.csv", index_col=0)
data3 = data1.append(data2, ignore_index=True)
data3 = data3.sample(frac=1, random_state=0)
data3.reset_index(inplace=True, drop=True)
y = list(data3.Label)
x = np.zeros((1,2,100,100)).astype(int)

for j in range(44):
    x_batch = np.zeros((1,2,100,100)).astype(int)
    for i in range(250):
        author1 = str(data3.Img1[i].astype(int))
        image1 = str(int(((data3.Img1[i] - data3.Img1[i].astype(int))*100).round()))
        
        author2 = str(data3.Img2[i].astype(int))
        image2 = str(int(((data3.Img2[i] - data3.Img2[i].astype(int))*100).round()))
        
        img1 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author1 + "_" + image1 + ".png")), (1,1,100,100)).astype(int)
        if author1==author2:
            if y[(j*250) + i] == 0:
                img2 = np.reshape(np.array(Image.open("Dataset/full_forg/forgeries_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
            else:
                img2 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        else:
            img2 = np.reshape(np.array(Image.open("Dataset/full_org/original_" + author2 + "_" + image2 + ".png")), (1,1,100,100)).astype(int)
        
        pair = np.append(img1, img2, axis=1)
        x_batch = np.append(x_batch, pair, axis = 0)
        print((250*j) + i)
    x_batch = np.delete(x_batch, 0, axis=0)
    x = np.append(x, x_batch, axis = 0)
    print("----------END OF BATCH----------")

x = np.delete(x, 0, axis=0)

np.save("Dataset/X_8020", x)
np.save("Dataset/Y_8020", y)
