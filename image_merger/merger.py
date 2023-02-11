import cv2
import os, sys
import math
from threading import Thread
import threading
import argparse
import numpy as np

progresses = {}

def printProgress(render_id, current, length):
    progresses[str(render_id)] = math.floor(current / length * 100)

    # print("\033[s", end="")
    # os.system('cls' if os.name == 'nt' else 'clear')

    # print("Progresses: ")

    print("\r" + "\t".join(
        [f"Render[{id}]: {progresses[id]}%" for id in progresses]
    ), end="\r")

    # print("\033[u", end="")

def get_images(image_folders):
    # image_folders = image_folder.split(";")

    images = []

    for image_folder in image_folders:
        images2 = sorted([os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")])

        images.extend(images2)

    return images

render_ids = 0

def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())

def render(args):
    
    images = get_images(args.folder)
    
    if args.size is None:
        frame = cv2.imread(images[0])
        # frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        height, width, layers = frame.shape
        size = (width, height)

    else:
        size = tuple(int(x) for x in args.size.split("x"))
        
    fourcc = cv2.VideoWriter_fourcc(*args.fourcc)
    print(fourcc)

    video = cv2.VideoWriter(args.out, fourcc, args.fps, size)

    print("Rendering video..")

    length = len(images)

    # used when multi threading
    global render_ids
    render_id = render_ids
    render_ids += 1

    last_image = None

    for i in range(length):
        
        # printProgress(render_id, i, length)
        print(f"\rProgess: {math.floor(i / length * 100)}%", end="\r")

        image = cv2.imread(images[i])

        # image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

        if image is None: 
            continue

        # remove duplicates
        if last_image is not None:
            if is_similar(last_image, image):
                continue

        last_image = image

        video.write(cv2.resize(image, size))

    # cv2.destroyAllWindows()
    video.release()

    print()
    # print(f"Successfully rendered video {render_id}!")
    print(f"Successfully rendered video!")

# threads = []

# def render(*args):
#    t = Thread(target=render_, args=args)
#    t.start()
#
#    global threads
#    threads.append(t)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    description = 'Merges pictures together into video'
    )

    parser.add_argument("folder", nargs="+", help="Folder where images are stored, can be passed multiple folders")
    parser.add_argument("-o", "--out", help="Output of the video", default="video.mp4")
    parser.add_argument("--fps", help="Fps of the video", default=20, type=int)
    parser.add_argument("-s", "--size", help="Size of the video, width x height")
    parser.add_argument("--fourcc", help="Encoding of the video", default="mp4v", type=str)

    args = parser.parse_args()
    
    render(args)
    # render("/home/joojn/Documents/Minecraft/dotminecraft_copy/screenshots;/home/joojn/Pictures/screenshots", "newer.mp4", 10)
