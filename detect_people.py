import cv2
from dialogs import select_dialog


def detect_people_old(image_path):
    body_classifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")
    lower_body_classifier = cv2.CascadeClassifier("haarcascade_lowerbody.xml")
    profile_face_classifier = cv2.CascadeClassifier("haarcascade_profileface.xml")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    lower_bodies = lower_body_classifier.detectMultiScale(gray, 1.2, 3)
    profile_faces = profile_face_classifier.detectMultiScale(gray, 1.2, 3)
    return len(bodies) > 0 or len(lower_bodies) > 0 or len(profile_faces) > 0


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


def main():
    image_path = select_dialog()
    if detect_people(image_path):
        print("People detected")
    else:
        print("No people detected")


if __name__ == "__main__":
    main()
