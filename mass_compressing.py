import os
import PIL
from PIL import Image
import threading

def to_part(lst: list, num: int):
    chunk_size = len(lst) // num
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def compress_images_default(directory=False, quality=60):
    if directory:
        os.chdir(directory)

    files = os.listdir()

    images = [file for file in files if file.endswith(('jpg', 'png'))]

    if not os.path.exists("compressed"):
        os.mkdir("compressed")

    for image in images:
        print("Current - ", image)

        img = Image.open(image)

        img.save(os.path.join("compressed", f"Compressed_{quality}q_" + image), optimize=True, quality=quality)


def compress_images(directory=False, quality=60, threads=5):
    if directory:
        os.chdir(directory)

    files = os.listdir()

    images = [file for file in files if file.endswith(('jpg', 'png'))]

    if not os.path.exists("compressed"):
        os.mkdir("compressed")

    lst_images = to_part(images, threads)

    for images in lst_images:
        kwargs = {"dir_to": directory, "images": images, "quality": quality, "prefix": ""}
        th = threading.Thread(target=compress, kwargs=kwargs)
        th.start()


def compress(dir_to, images, quality, prefix):
    if dir_to:
        os.chdir(dir_to)
    for image in images:
        print("Current - ", image)

        img = Image.open(image)

        img.save(os.path.join("compressed", prefix + image), optimize=True, quality=quality)