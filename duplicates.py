import os
from os.path import isdir, getsize


def get_duplicates(directory_path):
    """Производит поиск файлов-дубликатов в директории directory_path.
    Возвращает словарь, где ключ - это название файла-дубликата,
    а значение - список директорий, в которых находятся файлы-дубликаты
    с таким названием."""

    duplicates = dict()
    for current_dir, dir_list, file_list in os.walk(directory_path):
        for file in file_list:
            if file not in duplicates:
                duplicates[file] = [current_dir]
            else:
                sample_file_name = os.path.join(duplicates[file][0], file)
                current_file_name = os.path.join(current_dir, file)
                if getsize(current_file_name) == getsize(sample_file_name):
                    duplicates[file].append(current_dir)
    for key in list(duplicates):
        if len(duplicates[key]) == 1:
            duplicates.pop(key)
    return duplicates


if __name__ == '__main__':
    directory_path = input("В какой директории будем искать дубликаты? --- ")
    if not isdir(directory_path):
        print("Нет директории с таким именем! Завершение программы.")
        exit()
    d = get_duplicates(directory_path)
    for file, dirs in d.items():
        print("\nДанные файлы являются дубликатами:\n")
        for dir in dirs:
            print("%s/%s" % (dir, file))
