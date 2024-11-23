'''Задание №1
 ✔Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔Первое число int, второе - float разделены вертикальной чертой.
✔Минимальное число - -1000, максимальное - +1000.
✔Количество строк и имя файла передаются как аргументы функции. '''

from random import choice, randint, uniform, choices
from pathlib import Path
from typing import  TextIO
from string import  ascii_lowercase, digits
from os import chdir
import os

MIN_LIMIT = -1000
MAX_LIMIT = 1000
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def write_random_to_file(num_pairs: int, file_name: str | Path) -> None:
    with open(file_name, 'a', encoding='UTF-8') as f:
        for i in range(num_pairs):
            int_num = randint(MIN_LIMIT, MAX_LIMIT)
            float_num = uniform(MIN_LIMIT, MAX_LIMIT)
            f.write(f'{int_num:>4} | {float_num}\n')

# Задание №2
#  ✔Напишите функцию, которая генерирует псевдоимена.
# ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔Полученные имена сохраните в файл.

def generate_name(count: int, file_name: str | Path) -> None:
    for _ in range(count):
        first_chr = choice([-1, 1])
        name = ''
        for _ in range(randint(MIN_LEN, MAX_LEN)):
            if first_chr == -1:
                name += choice(CONSONANTS)
            else:
                name += choice(VOWELS)
            first_chr = choice([-1, 1])
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(name.title() + '\n')

# Задание №3
#  ✔Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
#  ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение:
#  ✔если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
#  ✔если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
#  ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле.
#  ✔При достижении конца более короткого файла, возвращайтесь в его начало.

def read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()

def converte(numbers: str, names: str, result: str) -> None:
    with (
        open(numbers, "r", encoding="utf-8") as f_number,
        open(names, "r", encoding="utf-8") as f_name,
        open(result, "w", encoding="utf-8") as f_result,
    ):
        len_names = sum(1 for _ in f_name)
        len_numbers = sum(1 for _ in f_number)
        for _ in range(max(len_numbers, len_names)):
            nums_str = read_or_begin(f_number)
            name = read_or_begin(f_name)
            num_i, num_f = nums_str.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_result.write(f"{name.lower()} {-mult} \n")
            else:
                f_result.write(f"{name.upper()} {int(mult)} \n")

# Задание №4
#  ✔Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
#  ✔расширение
#  ✔минимальная длина случайно сгенерированного имени, по умолчанию 6
#  ✔максимальная длина случайно сгенерированного имени, по умолчанию 30
#  ✔минимальное число случайных байт, записанных в файл, по умолчанию 256
#  ✔максимальное число случайных байт, записанных , в файл, по умолчанию 4096
#  ✔количество файлов, по умолчанию 42
#  ✔Имя файла и его размер должны быть в рамках переданного диапазона

def create_files(
        extension: str='bin',
        min_name=6,
        max_name=30,
        min_size=256,
        max_size=4096,
        num_files=2
) -> None:

    for i in range(num_files):
        # print()
        # print(ascii_lowercase)
        # print(choices(ascii_lowercase + digits + '_', k=5))
        name = ''.join(choices(ascii_lowercase + digits + '_', k=(randint(min_name, max_name))))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{extension}', 'wb') as file:
            file.write(data)

# Задание №5
#  ✔Доработаем предыдущую задачу.
# ✔Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔Расширения и количество файлов функция принимает в качестве параметров.
# ✔Количество переданных расширений может быть любым.
# ✔Количество файлов для каждого расширения различно.
# ✔Внутри используйте вызов функции из прошлой задачи

# Задание №6
#  ✔Дорабатываем функции из предыдущих задач.
# ✔Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

def gen_files(path: str|Path, **kwargs) -> None:
    if isinstance(path, str):
        path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)
    chdir(path)

    for extension, count in kwargs.items():
        create_files(extension=extension, num_files=count)

# Задание №7
#  ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки

def sort_files(sourse_directory):
    video_ext = ['.mp4', '.mov', 'mrv']
    image_ext = ['jpg', 'jpeg', 'png']
    text_ext = ['txt', 'doc', 'pdf']

    for file in os.listdir(sourse_directory):
        if os.path.isfile(os.path.join(sourse_directory, file)):
            file_ext = os.path.splitext(file)[1]


            if file_ext in video_ext:
                destination_folder = os.path.join(sourse_directory, 'Video')
            elif file_ext in image_ext:
                destination_folder = os.path.join(sourse_directory, 'Image')
            elif file_ext in text_ext:
                destination_folder = os.path.join(sourse_directory, 'Text')
            else:
                destination_folder = os.path.join(sourse_directory, 'Other')


            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            os.rename(os.path.join(sourse_directory, file), os.path.join(destination_folder, file))

if __name__ == '__main__':

    write_random_to_file(10, r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\random_numbers.txt') #1

    generate_name(10, Path(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\gen_name.txt')) #2

    converte(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\random_numbers.txt',
             r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\gen_name.txt',
             r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\result.txt') #3

    #create_files() #4

    gen_files(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\new', jpg=3, txt=2, bin=1) #5, 6

    source_directory = r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\new'
    sort_files(source_directory) #7
