import os
import time
 
file_text = open("short.dat", "r")
i=798
for file in file_text:
    tt_S =""
    yolo = open(file[:-1],"r")
    data = yolo.readlines()
    for info in data:
        tt_S += info[1:]
        a = tt_S.replace("\n","")
    line = f"{file[6:-5]}.jpg {len(data)}{a}\n"
    with open('info.dat', 'a') as f:
             f.write(f"{line}")
    print(f"{line}")
    i+=1

print(i)
    