import os
import string
import uuid
from os import listdir, urandom
from random import random
try:
    from ciphers.file_gen import create_file
except Exception:
    from file_gen import create_file

path = "D:\\test\\"


def cipher(read, rename, write_or_move, read_times, rename_times, write_times):
    files = listdir(path)
    def run():
        for filename in files:
            size = int(random() * 1024) + 128
            if read:
                f = open(path + filename, "rb")
                for _ in range(read_times):
                    f.read(1)
                f.close()

            f = open(path + filename, "wb")
            if write_or_move:
                for _ in range(write_times):
                    f.write(b"10")
                f.seek(size - 1)
                f.write(b"\1")
                f.close()

            else:
                create_file(path, "temp.txt")
                f2 = open(path + "temp.txt", "wb")
                f2.seek(size - 1)
                f2.write(b"\1")
                f2.close()
                f.close()
                os.remove(path + filename)
                os.rename(path + "temp.txt", path + filename)

            if rename:
                old_name = filename
                for _ in range(rename_times):
                    new_name = str(uuid.uuid4())
                    os.rename(path + old_name, path + new_name)
                    old_name = new_name
    return run


print(f"pid:{os.getpid()}")
t = int(input("Get number [0, 15]:"))
vars = [
    cipher(True, True, True, 1, 1, 1),
    cipher(True, False, True, 1, 1, 1),
    cipher(True, True, False, 1, 1, 1),
    cipher(True, False, False, 1, 1, 1),
    cipher(True, True, True, 10, 10, 10),
    cipher(True, False, True, 10, 10, 10),
    cipher(True, True, False, 10, 10, 10),
    cipher(True, False, False, 10, 10, 10),

    cipher(False, True, True, 1, 1, 1),
    cipher(False, False, True, 1, 1, 1),
    cipher(False, True, False, 1, 1, 1),
    cipher(False, False, False, 1, 1, 1),
    cipher(False, True, True, 10, 10, 10),
    cipher(False, False, True, 10, 10, 10),
    cipher(False, True, False, 10, 10, 10),
    cipher(False, False, False, 10, 10, 10)
]

vars[t]()
input("Wait:")

"""
а) читает \ не читает
б) переименовывает \ нет
в) пишет сразу \ замещает файл
"""
