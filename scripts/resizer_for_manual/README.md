# resizer_for_manual.py

Скрипт для работы с [фотками сфотканной бутылки](https://github.com/fominykhartur/bottles_dataset/tree/master/manual_wine)

---

Сначала скрипт делает квадрат нужного размера из изображения 

Потом он начинает его вертеть от 45 до 360 градусов с шагом 45

Отражает по горизонтали, и делает все тоже самое

Все файлы сохраняются в manual_wine_raw (нужно создать)

Потом файлы надо обратать скриптом [renamer.py](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts/renamer)
