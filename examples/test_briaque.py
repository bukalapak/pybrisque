#####################################################################################
import os
import glob

from brisque import BRISQUE

brisq = BRISQUE()

for f in glob.glob("*.jpg"):
    image_path = os.path.abspath(f)
    print('Reference image: %s %s' % (image_path, brisq.get_score(image_path)))

for f in glob.glob("*.bmp"):
    image_path = os.path.abspath(f)
    print('Reference image: %s %s' % (image_path, brisq.get_score(image_path)))

for f in glob.glob("*.png"):
    image_path = os.path.abspath(f)
    print('Reference image: %s %s' % (image_path, brisq.get_score(image_path)))

