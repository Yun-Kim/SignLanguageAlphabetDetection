from PIL import Image
import os

path_to_asl_alphabet = r"<path>"

def crop_img(filepath):
    im = Image.open(filepath)

    w, h = im.size
    offset = 5

    # left top right bot
    im.crop((offset, offset, w-offset, h-offset)).save(filepath)


for subdir, dirs, files in os.walk(path_to_asl_alphabet):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".jpg"):
            crop_img(filepath)

