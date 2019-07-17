# bottles_dataset
Датасет содержащий бутылки алкоголя разбитые на категории

---


**[bottles_original](https://github.com/fominykhartur/bottles_dataset/tree/master/bottles_original)** - оригиналы скачанные с [amwine.ru](https://amwine.ru) помощью [parser.py]()

**[bottles_sized](https://github.com/fominykhartur/bottles_dataset/tree/master/bottles_sized)** - фотографии разбитые на train и validation в 224х224

**[bottles_sized_450](https://github.com/fominykhartur/bottles_dataset/tree/master/bottles_sized_450)** - фотографии разбитые на train и validation в 448х448

**[bottles_sized_450_200](https://github.com/fominykhartur/bottles_dataset/tree/master/bottles_sized_450_200)** - фотографии разбитые на train и validation в 448х448, все категории папки train по 200 фоток, validation по 20

**[manual_wine](https://github.com/fominykhartur/bottles_dataset/tree/master/manual_wine)** - фотографии одной бутылки вина разбитые на train и validation, все фотографии в оригинальном разрешении 

**[manual_wine_before_shuffle](https://github.com/fominykhartur/bottles_dataset/tree/master/manual_wine_before_shuffle)** - оригиналы фотографий одной бутылки вина 

**[manual_wine_sized](https://github.com/fominykhartur/bottles_dataset/tree/master/manual_wine_sized)** - оригиналы фотографий одной бутылки вина, разбитые на train и validation. На каждую фотографию есть отраженная по горизонтали фотография и на их основе все фотографии поверчены с шагом 45 градусов. Все в 224х224

**[manual_wine_sized_450](https://github.com/fominykhartur/bottles_dataset/tree/master/manual_wine_sized_450)** - оригиналы фотографий одной бутылки вина, разбитые на train и validation. На каждую фотографию есть отраженная по горизонтали фотография и на их основе все фотографии поверчены с шагом 45 градусов. Все в 448х448

**[scripts](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts)** - папка с использованными скриптами

---

**[parser.py](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts/parser)** - скрипт для скачки с [amwine.ru](https://amwine.ru/)

**[resizer.py](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts/resizer)** - Скрипт для конвертирования .png в .jpg и превращения фотографию в квадрат нужного размера

**[resizer_for_manual.py](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts/resizer_for_manual)** - Скрипт для конвертирования .png в .jpg и превращения фотографий из папки  в квадрат нужного размера

**[mover.py](https://github.com/fominykhartur/bottles_dataset/blob/master/scripts/mover)** - Скрипт для смешения фотографии по диагонали и добивания до n количества фоток в папке

**[renamer.py](https://github.com/fominykhartur/bottles_dataset/tree/master/scripts/renamer)** - Скрипт для перемешивания фотографий сфотканной бутылки
