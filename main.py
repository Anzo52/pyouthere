from detectors import detect_in_dir, detect_people
from dialogs import select_dialog
from organize import *


def print_file_count(with_people, no_people):
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


def dir_func():
    dir_path = select_dialog("opendir")
    with_people, no_people = detect_in_dir(dir_path)
    print_file_count(with_people, no_people)
    print("Organize files?")
    organize_my_files = input("y/n: ")
    if organize_my_files == "y":
        organize_files(with_people, no_people)


def main():
    print("1) Single file")
    print("2) Directory")
    print("3) Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        file_path = select_dialog()
        if detect_people(file_path):
            print("People detected")
        else:
            print("No people detected")
    elif choice == "2":
        dir_func()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        main()


if __name__ == "__main__":
    main()
