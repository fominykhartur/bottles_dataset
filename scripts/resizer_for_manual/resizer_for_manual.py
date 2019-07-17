from PIL import Image
from os import listdir
import os
import re

path = input("Введите путь\n")
count = 1
for i in listdir(path):
    new_path = path + "\\" + i

    for j in listdir(new_path):
        try:
            print("{}\\{}".format(new_path, j))
            img_original = Image.open("{}\\{}".format(new_path, j))
            x, y = img_original.size
            size = max(x, y)
            img_changed = Image.new('RGB', (size, size), (255, 255, 255))
            img_changed.paste(img_original, (int((size - x) / 2), int((size - y) / 2)))

            size = 448
            img_changed = img_changed.resize((size, size), Image.ANTIALIAS)

            img_changed.save("bottles_dataset\\manual_wine_raw\\raw_{}.jpg".format(count))

            for rot in range(45, 360, 45):
                count += 1
                img_changed.rotate(rot).save("bottles_dataset\\manual_wine_raw\\raw_{}.jpg".format(count))
            count += 1
            img_changed = img_changed.transpose(Image.FLIP_LEFT_RIGHT)
            img_changed.save("bottles_dataset\\manual_wine_raw\\raw_{}.jpg".format(count))
            for rot in range(45, 360, 45):
                count += 1
                img_changed.rotate(rot).save("bottles_dataset\\manual_wine_raw\\raw_{}.jpg".format(count))
            print(str(j) + " DONE")
            count += 1
        except FileNotFoundError or FileExistsError:
            print(str(j) + " doesn't exists")
            count += 1
