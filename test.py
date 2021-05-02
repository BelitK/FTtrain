import os
texts = os.listdir("train")
for text in texts:
    if text.endswith(".txt"):
        yolo = open(f"train/{text}")
        lines = yolo.readlines()
        if len(lines)>1:
            with open('long.dat', 'a') as f:
               f.write(f"train/{text}\n")
