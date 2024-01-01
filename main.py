from detectors import detect_in_dir, detect_people
from dialogs import select_dialog
from organize import to_org


def print_file_count(with_people, no_people):
    print(f"{len(with_people)} Files with people: {with_people}")
    print(f"{len(no_people)} Files without people: {no_people}")
    print(f"Total files: {len(with_people) + len(no_people)}")


def dir_func():
    dir_path = select_dialog("opendir")
    with_people, no_people = detect_in_dir(dir_path)
    print_file_count(with_people, no_people)
    return with_people, no_people


def main_menu():
    options = ["1) Single file", "2) Directory", "3) Exit"]
    print("\n".join(options))



def get_actions():
    return {
        "1": lambda: select_dialog() and print("People detected")
        if detect_people(select_dialog())
        else print("No people detected"),
        "2": lambda: to_org(*dir_func()),
        "3": exit,
    }


def main():
    actions = get_actions()
    while True:
        main_menu()
        choice = input("Enter choice: ")
        action = actions.get(choice, lambda: print("Invalid choice"))
        action()


if __name__ == "__main__":
    main()
