from PIL import Image
import os
import PIL
import glob

i=1144
resize = (800,800)
image_list = os.listdir("Neutral1")


for image in image_list:
    data = Image.open(f"Neutral1/{image}")
    out = data.resize(resize)
    out.save(f"negatives/{i}.png")
    i+=1
print(i)

#final 1243 negative pics 1427 positives