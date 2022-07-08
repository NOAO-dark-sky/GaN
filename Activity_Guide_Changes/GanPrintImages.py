from docx import Document
from PIL import Image


def open_word_doc(filename):
    document = Document(filename)
    return document

def openImage():
    pass

#crops an image based on the magnitude, saves image as png
def cutStarChart(filename):
    
    cut_points = {
            "Mag0" : (80,80,826,596),
            "Mag1" : (834,80,1577,596),
            "Mag2" : (80,604,826,1119),
            "Mag3" : (834,604,1577,1119),
            "Mag4" : (80,1127,826,1642),
            "Mag5" : (834,1127,1577,1642),
            "Mag6" : (80,1651,826,2166),
            "Mag7" : (834,1651,1577,2166)
            }
    for key, value in cut_points.items():
        im = Image.open(filename)
        im.crop(value).save(key + ".png")

    return

def bigTable():
    pass

def littleTable():
    pass

