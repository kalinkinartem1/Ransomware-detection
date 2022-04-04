import os
from random import random
file_pathes = ["D:test\\"]

count = 100


def create_dir(__file_path):
    directory = os.path.dirname(__file_path)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)


def create_file(path, name):
    filename = path + name + ".txt"
    f = open(filename, "w+")
    f.write("test\n"*10)
    f.close()


def gen_files():
    for file_path in file_pathes:
        create_dir(file_path)
        for i in range(0, count):
            create_file(file_path, str(i))
# gen_files()