#%%
import os
import time
from datetime import datetime
from PIL import ImageGrab
import argparse
#%%
parser = argparse.ArgumentParser()
parser.add_argument("delay", type=int, help="How long to wait between photos")
parser.add_argument("maxphotos", type=int, nargs="?", help="How many photos to stop after")
if not os.path.isdir("screenshots"):
    os.mkdir("screenshots")
#%%
def takeScreenshots(delay, maxphotos=None):
    i = 0
    while maxphotos == None or i < maxphotos:
        i += 1
        screen = ImageGrab.grab()
        filename = "screenshots/" + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".png"
        screen.save(filename)
        time.sleep(delay)
# %%
if __name__ == "__main__":
    args = parser.parse_args()
    print(f"Taking a screenshot every {args.delay} seconds")
    if args.maxphotos:
        print(f"Max of {args.maxphotos} screenshots")
    print(f"Saving screenshots in {os.getcwd()}\screenshots")
    takeScreenshots(args.delay, args.maxphotos)
    print("Done screenshotting!")