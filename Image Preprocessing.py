from PIL import Image

for i in range(55):
    for j in range(24):
        filename = "original_" + str(i+1) + "_" + str(j+1) + ".png"
        img = Image.open("Original/full_org/" + filename)
        img = img.resize((100,100))
        img = img.convert('L')
        img = img.point(lambda p: 255 if p>200 else 0)
        img.save("Dataset/full_org/" + filename)
        
        filename = "forgeries_" + str(i+1) + "_" + str(j+1) + ".png"
        img = Image.open("Original/full_forg/" + filename)
        img = img.resize((100,100))
        img = img.convert('L')
        img = img.point(lambda p: 255 if p>225 else 0)
        img.save("Dataset/full_forg/" + filename)
        
        print(str(i) + ", " + str(j))