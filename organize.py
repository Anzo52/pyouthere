# script to organize images into folders based on return from detect_batch.py

import os
import shutil


def make_directory(dir_path, dir_name):
    directory = os.path.join(dir_path, dir_name)
    os.makedirs(directory, exist_ok=True)
    return directory


def move_files(file_list, dir_path):
    for file in file_list:
        print(f"Moving {file} to {dir_path}")
        shutil.move(file, dir_path)
