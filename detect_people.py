import cv2
from tkinter import Tk, filedialog

tk_instance = Tk()
tk_instance.withdraw()


def detect_features(classifier_path, image_path):
    classifier = cv2.CascadeClassifier(classifier_path)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, 1.2, 3)
    return len(features) > 0


def detect_people(image_path):
    classifiers = [
        "haarcascade_fullbody.xml",
        "haarcascade_lowerbody.xml",
        "haarcascade_profileface.xml",
        "haarcascade_frontalface_alt.xml",
        "haarcascade_upperbody.xml",
    ]
    return any(detect_features(c, image_path) for c in classifiers)


def select_image_dialog():
    return filedialog.askopenfilename()


def main():
    image_path = select_image_dialog()
    if detect_people(image_path):
        print("People detected")
    else:
        print("No people detected")


if __name__ == "__main__":
    main()
