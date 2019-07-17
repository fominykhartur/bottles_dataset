from os import listdir
from PIL import Image
import os

path = input("введите путь\n")
for i in listdir(path):
    count = 1
    new_path = "{}\\{}".format(path, i)
    print(new_path + " " + str(len(listdir(new_path))))
    if len(listdir(new_path)) < 200:
        if not os.path.exists("bottles_dataset\\bottles_sized_450\\train_test\\{0}".format(i)):
            os.makedirs("bottles_dataset\\bottles_sized_450\\train_test\\{0}".format(i))
        for j in listdir(new_path):
            pic = "{}\\{}".format(new_path, j)

            pic_original = Image.open(pic)

            pic_new = Image.new("RGB", (448, 448), (255, 255, 255))
            pic_original.save("bottles_dataset\\bottles_sized_450\\train_test\\{0}\\{0}_{1}.jpg".format(i, count))
            count += 1
        count += 1
        for j in listdir("bottles_dataset\\bottles_sized_450\\train_test\\{0}".format(i)):
            print("bottles_dataset\\bottles_sized_450\\train_test\\{0}\\{1}".format(i, j))
            if len(listdir("bottles_dataset\\bottles_sized_450\\train_test\\{0}".format(i))) < 200:
                pic = "bottles_dataset\\bottles_sized_450\\train_test\\{0}\\{1}".format(i, j)
                pic_original = Image.open(pic)

                pic_new = Image.new("RGB", (448, 448), (255, 255, 255))
                for shift in range(10, 30, 5):
                    pic_new.paste(pic_original, (shift, shift))
                    pic_new.save("bottles_dataset\\bottles_sized_450\\train_test\\{0}\\{0}_{1}.jpg".format(i, count))
                    # print("bottles_dataset\\bottles_sized_450\\train_test\\{0}\\{0}_{1}.jpg".format(i,count))
                    count += 1
