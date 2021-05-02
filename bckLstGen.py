import os
def createbcklist():
    for file_type in ['non_fire_images']:

        for img in os.listdir(file_type):

            line = file_type + '/' + img + '\n'
            with open('background.txt', 'a') as f:
                f.write(line)

createbcklist()