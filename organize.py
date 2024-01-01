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


def make_and_move(dir_path, dir_name, file_list):
    directory = make_directory(dir_path, dir_name)
    move_files(file_list, directory)


def organize_files(with_people, no_people):
    dir_path = os.path.dirname(with_people[0])
    make_and_move(dir_path, "with_people", with_people)
    make_and_move(dir_path, "no_people", no_people)
    print("Done")


def to_org(with_people, no_people):
    print("Organize files?")
    organize_my_files = input("y/n: ")
    if organize_my_files == "y":
        organize_files(with_people, no_people)
    else:
        print("Files not organized")