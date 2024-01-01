from detectors import detect_in_dir, detect_people
from dialogs import select_dialog


def detect_in_directory():
    dir_path = select_dialog("directory")
    with_people, no_people = detect_in_dir(dir_path)
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


def detect_image():
    image_path = select_dialog()
    if detect_people(image_path):
        print("People detected")
    else:
        print("No people detected")