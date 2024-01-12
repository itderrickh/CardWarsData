from PIL import Image
import os

path = 'F:\CornDome\data\images'

def resize():
    for item in os.listdir(path):
        finalpath = os.path.join(path, item)
        if os.path.isfile(finalpath) and finalpath.endswith(".jpg"):
            im = Image.open(finalpath)
            if im.size[0] != 370 and im.size[1] != 516:
                print('Resizing: ' + item)
                imResize = im.resize((370,516), Image.LANCZOS)
                imResize.save(finalpath, 'JPEG', quality=90)

        if os.path.isfile(finalpath) and finalpath.endswith(".png"):
            im = Image.open(finalpath)
            if im.size[0] != 370 and im.size[1] != 516:
                print('Resizing: ' + item)
                imResize = im.resize((370,516), Image.LANCZOS)
                imResize.save(finalpath, 'PNG', quality=90)

resize()