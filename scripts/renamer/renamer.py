from os import listdir
import os
import random

path = input("введите путь\n")
list = listdir(path)
#print(list)
#print("\n\n\n")
random.shuffle(list)
#print(list)
num = 1
for i in list:
    os.rename(path + "\\" + i, "bottles_dataset\\manual_wine_shuffled\\manual_" + str(num) + ".jpg")
    num += 1
