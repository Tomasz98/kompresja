import os
import sys
from PIL import Image

def changeFormat(file):
    try:
        temp_file = file.split('/')[-1].split('.')[0]
    except:
        temp_file = file.split('.')[0]
    new_file = "/".join(file.split('/')[0:-1])+"/"+temp_file+".jpeg"
    print(new_file)



    img = Image.open(file[1:])
    img.save(new_file[1:])


def compressMe(file, verbose=False):

    filepath = os.path.join(os.getcwd(),
                            file)
    picture = Image.open(filepath)
    picture.save("Compressed_" + file,
                 "JPEG",
                 optimize=True,
                 quality=10)

def main():
    verbose = False
    if (len(sys.argv) > 1):

        if (sys.argv[1].lower() == "-v"):
            verbose = True

    # finds current working dir
    cwd = os.getcwd()
    formats = ('.jpg', '.jpeg', '.png')


    for file in os.listdir(cwd):

        # If the file format is JPG or JPEG
        if os.path.splitext(file)[1].lower() in formats:
            print('compressing', file)
            compressMe(file, verbose)

    print("Done")


