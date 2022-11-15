import platform
import os
from PIL import Image
# This code is based on the pyheif ver. 0.7.0
# import pyheif

# These are supported heif extensions by the library. (https://github.com/carsales/pyheif/blob/master/libheif/heif.h)
heifExtensions = ["heic", "heix", "hevc", "heim", "heis", "hevm", "hevs", "mif1", "msf1", "avif", "avis"]

def main():
    osCat = platform.system()
    files = os.listdir(os.getcwd())
    splitPath = []
    heicFiles = []
    
    if osCat.lower() == "windows":
        import pillow_heif
    else:
        import pyheif

    for file in files:
        if(osCat.lower() == "windows"):     # Windows
            splitPath = file.split('\\')
        else:   # Mac or Linux
            splitPath = file.split('/')
        if(splitPath[-1].split('.')[-1].lower() in heifExtensions):     # File name. (ex. img.jpg)
            heicFiles.append(file)
    print(heicFiles)
    for file in heicFiles:
        heif_file = pyheif.read(file)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        splitPath = file.split('.')
        splitPath[-1] = ".jpg"
        savePath = ''.join(splitPath)
        image.save(savePath, "JPEG")
        print(savePath + "saved!")

if name == "main":
    main()