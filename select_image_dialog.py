from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory


def select_image_dialog():
    Tk().withdraw()
    return askopenfilename()


def file_dialog():
    Tk().withdraw()
    return askdirectory()