from detectors import detect_people
from dialogs import select_dialog


def main():
    image_path = select_dialog()
    if detect_people(image_path):
        print("People detected")
    else:
        print("No people detected")


if __name__ == "__main__":
    main()
