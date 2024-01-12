from PIL import Image
import os, sys

path = 'F:\CornDome\data\images'

def resize():
    for item in os.listdir(path):
        finalpath = os.path.join(path, item)
        if os.path.isfile(finalpath) and finalpath.endswith(".jpg"):
            im = Image.open(finalpath)
            f, e = os.path.splitext(finalpath)
            imResize = im.resize((370,516), Image.LANCZOS)
            imResize.save(finalpath, 'JPEG', quality=90)

resize()