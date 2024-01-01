# script to organize images into folders based on return from detect_batch.py

from detect_batch import detect_in_dir
import os
import shutil
from select_image_dialog import select_dialog


def make_directory(dir_path, dir_name):
    directory = os.path.join(dir_path, dir_name)
    os.makedirs(directory, exist_ok=True)
    return directory


def move_files(file_list, dir_path):
    for file in file_list:
        print(f"Moving {file} to {dir_path}")
        shutil.move(file, dir_path)


def main():
    dir_path = select_dialog("directory")
    with_people, no_people = detect_in_dir(dir_path)
    directories = {
        "with_people": with_people,
        "no_people": no_people,
    }
    for dir_name, files in directories.items():
        target_dir = make_directory(dir_path, dir_name)
        move_files(files, target_dir)
    print(f"(len(with_people)) Files with people: {with_people}")
    print(f"(len(no_people)) Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


if __name__ == "__main__":
    main()
