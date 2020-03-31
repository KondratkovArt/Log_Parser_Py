import os
from os import listdir
from os.path import isfile, join
filePath = input("Введите путь к файлу или папке с файлами: ")
incorrect_path = True
all_lines = []


def read_dir():
    files = [join(filePath, f) for f in listdir(filePath) if isfile(join(filePath, f))]
    global all_lines
    for file in files:
        if file.endswith('.txt'):
            f = open(file)
            for line in f:
                all_lines.append(line)


def read_file():
    file = open(filePath)
    global all_lines
    for line in file:
        all_lines.append(line)


while incorrect_path:
    if os.path.exists(filePath):
        incorrect_path = False
    else:
        filePath = input("Введён некорректный путь. Введите путь заново: ")

read_dir() if os.path.isdir(filePath) else read_file()
all_lines = [line.rstrip() for line in all_lines]