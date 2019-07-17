import requests
import re

url, bottle_name = input("вставьте ссылку\n") + '?page=', input("введите напиток и доп.инфу через _\n")

pattern = r'\/upload\/iblock\/(?!993\/99396097ae75c20bd0447e51bc881716|d15\/d15362fdfbf492a82f0d43334b6e6287|' \
          r'a53\/a5308380eee93038760518e8438d954f|f41\/f41dc56e746b4a941725e582a66a1382|' \
          r'aca/acaf8957f0d5a97a7a8863a5c206ed90.png)[\w/]+.png'
count = 1

content = requests.get(url + '1').text
last_page = int(re.search(r'\d+', (re.search(r'TotalCount\s+= \d+', content)).group(0)).group(0)) / 18
if last_page % 100 != 0:
    last_page = int(last_page) + 1
print(last_page)

for j in range(1, last_page + 1):
    url_pages = url + str(j)

    content = requests.get(url_pages).text

    match = re.findall(pattern, content)

    print("страниа номер " + str(j) + " количество бутылок " + str(len(match)))

    for i in range(len(match)):
        with open('bottles_dataset/bottles_original/test/{}_{}.png'.format(bottle_name, str(count)), 'wb') as pic:
            pic.write(requests.get('https://amwine.ru' + match[i]).content)
            print(str(count) + ' Done ' + 'https://amwine.ru' + match[i])
            count += 1
