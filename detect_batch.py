from detectors import detect_in_dir
from dialogs import select_dialog


def main():
    dir_path = select_dialog("directory")
    with_people, no_people = detect_in_dir(dir_path)
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


if __name__ == "__main__":
    main()
