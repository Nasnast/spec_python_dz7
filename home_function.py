'''Задание 1. Функцию группового переименования файлов.
 Напишите функциюгруппового переименования файлов. Она должна:
 1. принимать параметр желаемое конечное имя файлов. При
 переименовании в конце имени добавляется порядковый номер.
 2. принимать параметр количество цифр в порядковом номере.
 3. принимать параметр расширение исходного файла. Переименование
 должно работать только для этих файлов внутри каталога.
 4. принимать параметр расширение конечного файла.
 5. принимать диапазон сохраняемого оригинального имени.
 Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
 Книмприбавляется желаемое конечное имя, если оно передано. Далее счётчик
 файлов ирасширение. 3.Соберите из созданных на уроке и в рамках домашнего
 задания функций пакет для работы с файлами'''


from pathlib import  Path
import os
import zipfile
import  time

def group_rename_files(directory, new_name, count, old_extension, new_extension, name_range):

    if not os.path.exists(directory):
        print(f"Каталог'{directory}'не найден.")

    files = []
    for f in os.listdir(directory):
        if f.endswith(old_extension):
                files.append(f)
    if not files:
        print(f'файлы с таким расширением {old_extension} не найдены')
        return False

    format_string = f'{{:0{count}d}}'

    for i, file_name in enumerate(files, start=1):
        base_name = os.path.splitext(file_name)[0]
        if name_range:
            start, stop = name_range
            extracted_name  = base_name[start -1:stop]
        else:
            extracted_name = base_name
        new_file_name = f'{extracted_name}{new_name}{format_string.format(i)}{new_extension}'

        old_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_file_name)

        os.rename(old_file_path, new_file_path)
        print(f'переименован файл {file_name} в {new_file_name}')


'''Задача2.Создание архива каталога
Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
 должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
 должен включать все файлы и подпапки исходного каталога'''

def zip_directory(directory, zip_directory):
    with zipfile.ZipFile(zip_directory, 'w', zipfile.ZIP_DEFLATED) as z_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                z_file.write(file_path, os.path.relpath(file_path, directory))

"""Задача3.Удаление старых файлов
 Напишите скрипт,который удаляет файлы в указанном каталоге,которые не
 изменялись более заданного количества дней.Скрипт должен принимать путь к
 каталогу и количество дней"""

def del_old_file(directory: str|Path, days: int) -> None:

    now_time = time.time()
    days_in_sec = days * 86400
    limit_time = now_time - days_in_sec

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file) # путь в файлу
            file_time = os.path.getmtime(file_path) # дата изменения файла
            if limit_time > file_time:
                os.remove(file_path)
                print(f'файл {file_path} удален ')
            else:
                print(f'не найдены файлы старше {days} дней')

"""Задача4. Поиск файлов по расширению
Напишите функцию, которая находит и перечисляет все файлы с заданным
расширением в указанном каталоге и всех его подкаталогах. Функция должна
принимать путь к каталогу и расширение файла"""

def find_file(directory: str|Path, extension: str) -> None:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))
if __name__ == '__main__':

    directory = Path(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files\Other')
    new_name = 'file'
    count = 2
    old_extension = '.pdf'
    new_extension = '.txt'
    name_range = [2, 6]
    group_rename_files(directory,new_name,count, old_extension,new_extension,name_range) #1

    zip_directory(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files',
                  r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files.zip') #2

    del_old_file(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files', 1) #3

    find_file(r'D:\Anastasi\geekBrains\Погружение в Python 07.10.2024\Sem7\DZ7\DZ7_files', "txt")




