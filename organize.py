# script to organize images into folders based on return from detect_batch.py

from detect_batch import detect_in_dir
import os
import shutil
from select_image_dialog import file_dialog


def make_no_people_dir(dir_path):
    no_people_dir = os.path.join(dir_path, "no_people")
    if not os.path.exists(no_people_dir):
        os.mkdir(no_people_dir)
    return no_people_dir


def make_with_people_dir(dir_path):
    with_people_dir = os.path.join(dir_path, "with_people")
    if not os.path.exists(with_people_dir):
        os.mkdir(with_people_dir)
    return with_people_dir


def move_files(file_list, dir_path):
    for file in file_list:
        print(f"Moving {file} to {dir_path}")
        shutil.move(file, dir_path)


def main():
    dir_path = file_dialog()
    with_people, no_people = detect_in_dir(dir_path)
    no_people_dir = make_no_people_dir(dir_path)
    with_people_dir = make_with_people_dir(dir_path)
    move_files(no_people, no_people_dir)
    move_files(with_people, with_people_dir)
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


if __name__ == "__main__":
    main()
