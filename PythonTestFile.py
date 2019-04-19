import pathlib
import os


def recursive_delete():

    folder_path = 'C:\\Python\\TestDir\\'
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            os.remove(folder_path + file_name)

            recursive_delete()