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
    detection_results = {'with_people': [], 'no_people': []}
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if detect_people(file_path):
            print(f"People detected in {file_path}")
            detection_results['with_people'].append(file_path)
        else:
            print(f"No people detected in {file_path}")
            detection_results['no_people'].append(file_path)
    return detection_results["with_people"], detection_results["no_people"]


def detect_features(classifier_path, image_path):
    classifier = cv2.CascadeClassifier(classifier_path)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray, 1.2, 3)
    return len(features) > 0
