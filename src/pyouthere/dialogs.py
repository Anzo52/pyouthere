from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory


def select_dialog(dialog_type="openfile"):
    Tk().withdraw()
    return askopenfilename() if dialog_type == "openfile" else askdirectory()
