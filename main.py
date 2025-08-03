import os
import pathlib
import sys

import tqdm
from PIL import Image

if len(sys.argv) != 2:
    raise Exception("Too few arguments passed to command line, expected 1, found 0")

path = pathlib.Path(sys.argv[1])

img = Image.open(path)
pixels = list(img.getdata())
size = len(pixels)
img.close()

pixels.sort()

simg = Image.new(img.mode, img.size, (0, 0, 0, 0) if img.mode == "RGBA" else 0)
for i in tqdm.tqdm(range(size)):
    y = i // simg.height
    x = i % simg.width
    px = pixels[i]
    simg.putpixel((x, y), px)

if not os.path.exists("result"):
    os.mkdir("result")

filename, extension = path.name.split(".", 1)
simg.save(f"result/{filename}-sorted.{extension}")
