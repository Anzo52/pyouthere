# pyouthere

## Overview

pyouthere is a Python application that checks if a human is present in a picture. It utilizes various Haar cascades for detecting different parts of the human body and faces in images.

## Features

- Detection of humans in images using Haar cascades.
- Support for detecting full body, upper body, lower body, frontal face, and profile face.
- Functionality to process a single image or a directory of images.
- Organizing images into folders based on detection results.

## Requirements

The application requires the following Python packages:

- numpy==1.26.2
- opencv-python==4.9.0.80
- simple-term-menu==1.6.4

These can be installed using the `requirements.txt` file.

## Usage

To use pyouthere, you can either process a single file or an entire directory of images. The application will then detect the presence of people in these images and organize them accordingly.

### Main Functions

- `detect_people(image_path)`: Detects people in a single image.
- `detect_in_dir(dir_path)`: Detects people in all images within a specified directory.
- `organize_files(with_people, no_people)`: Organizes images into 'with_people' and 'no_people' directories.

### Running the Application

Run `main.py` to start the application. You will be presented with options to choose between processing a single file, a directory, or exiting the application.

## Haar Cascades

The application uses several Haar cascade files for detection:

- haarcascade_frontalface_alt.xml
- haarcascade_fullbody.xml
- haarcascade_lowerbody.xml
- haarcascade_profileface.xml
- haarcascade_upperbody.xml

## Contributing

Contributions to pyouthere are welcome. Please ensure to follow the coding standards and guidelines of the project.

## License

This project is licensed under the [MIT License](https://github.com/Anzo52/pyouthere/blob/main/LICENSE).
