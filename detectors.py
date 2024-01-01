import os
import cv2


def detect_people(image_path):
    classifiers = [
        "haarcascade_fullbody.xml",
        "haarcascade_lowerbody.xml",
        "haarcascade_profileface.xml",
        "haarcascade_frontalface_alt.xml",
        "haarcascade_upperbody.xml",
    ]
    return any(detect_features(c, image_path) for c in classifiers)


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


def detect_features(classifier_path, image_path):
    classifier = cv2.CascadeClassifier(classifier_path)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, 1.2, 3)
    return len(features) > 0
