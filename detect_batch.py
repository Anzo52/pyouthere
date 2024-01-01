from detect_people import detect_people
import os
from select_image_dialog import select_dialog


def detect_in_dir(dir_path):
    file_paths = []
    with_people = []
    no_people = []
    for file_name in os.listdir(dir_path):
        print(file_name)
        file_paths.append(os.path.join(dir_path, file_name))
    for file in file_paths:
        if detect_people(file):
            print(f"People detected in {file}")
            with_people.append(file)
        else:
            print(f"No people detected in {file}")
            no_people.append(file)
    return with_people, no_people


def main():
    dir_path = select_dialog("directory")
    with_people, no_people = detect_in_dir(dir_path)
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


if __name__ == "__main__":
    main()
