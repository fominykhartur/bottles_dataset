from PIL import Image
from os import listdir
import os
import re


def remove_transparency(im, bg_colour=(255, 255, 255)):
    # Only process if image has transparency (http://stackoverflow.com/a/1963146)
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im


path_dir = input("Введите путь\n")

with open('log.txt', 'w') as log:
    log.write(path_dir + " " + str(len(listdir(path_dir))) + "\n")

for i in listdir(path_dir):
    path = path_dir + "\\" + i
    print(path)
    new_path = re.findall(r'[^\\]+', path)

    print(listdir(path))

    first_num, last_num = min(map(int, re.findall(r'\d+', ''.join(listdir(path))))), \
                          max(map(int, re.findall(r'\d+', ''.join(listdir(path)))))

    if len(new_path) == 8:
        filename = (re.match(r'[a-zA-Z]+', listdir(path)[0])).group(0)
        new_path = "bottles_dataset/bottles_sized_450/{0}/{1}".format(new_path[6], new_path[7])
    else:
        filename = (re.match(r'[a-zA-Z]+', listdir(path)[0])).group(0)
        new_path = "bottles_dataset/bottles_sized_450/" + new_path[6]
    print("bottles_dataset/bottles_sized_450/{}".format(new_path))

    print(new_path)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for i in range(first_num, last_num + 1):
        try:
            print('{}\\{}_{}.jpg'.format(path, filename, str(i)))
            img_original = Image.open('{}\\{}_{}.png'.format(path, filename, str(i)))

            x, y = img_original.size
            size = max(x, y)
            img_changed = Image.new('RGBA', (size, size), (255, 255, 255))
            img_changed.paste(img_original, (int((size - x) / 2), int((size - y) / 2)))

            size = 448
            img_changed = img_changed.resize((size, size), Image.ANTIALIAS)
            img_rgb = Image.new('RGB', (size, size), (255, 255, 255))
            img_rgb = remove_transparency(img_changed).convert("RGB")
            img_rgb.save("{}/{}_{}.jpg".format(new_path, filename, str(i)), "JPEG", quality=95)
            print(str(i) + " DONE")
        except FileNotFoundError or FileExistsError:
            print(str(i) + " doesn't exists")
            i += 1
    print(path + " DONE")
    with open('log.txt', 'a') as log:
        log.write(path + " " + str(len(listdir(path))) + " " + str(len(listdir(new_path))) + "\n")
