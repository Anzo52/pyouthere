from detectors import detect_in_dir, detect_people
from dialogs import select_dialog
from organize import to_org


def print_files_and_count(with_people, no_people):
    print("Files with people:")
    print("\n".join(with_people))
    print("Files without people:")
    print("\n".join(no_people))
    print(f"Files with people: {len(with_people)}")
    print(f"Files without people: {len(no_people)}")
    print(f"Total files: {len(with_people) + len(no_people)}")


def process_directory():
    dir_path = select_dialog("opendir")
    with_people, no_people = detect_in_dir(dir_path)
    print_files_and_count(with_people, no_people)
    to_org(with_people, no_people)




def select_dialog_and_detect_people():
    file_path = select_dialog()
    if detect_people(file_path):
        print("People detected")
    else:
        print("No people detected")


def main():
    actions = {
        "1": select_dialog_and_detect_people,
        "2": process_directory,
        "3": exit,
    }
    options = ["1) Single file", "2) Directory", "3) Exit"]
    while True:
        print("\n".join(options))
        choice = input("Enter choice: ")
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()


if __name__ == "__main__":
    main()
