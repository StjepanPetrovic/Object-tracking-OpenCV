import os
import cv2

from zipfile import ZipFile
from urllib.request import urlretrieve

from matplotlib import pyplot as plt


def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assets....", end="")

    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)


URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)
else:
    print("\nZip already exists.")

# Read image as gray scale.
cb_img = cv2.imread("checkerboard_18x18.png", 0)

# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]
print(cb_img)

# Read in image
coke_img = cv2.imread("coca-cola-logo.png", 1)

# print the size (height, width, number of color channels - red, green, blue) of image
print("\nImage size (H, W, C) is:", coke_img.shape)

# print data-type of image
print("Data type of image is:", coke_img.dtype)

plt.imshow(coke_img)
plt.show()
