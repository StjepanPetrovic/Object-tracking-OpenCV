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

# Split the image into the B,G,R components
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)

# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)

img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h, s, v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20, 5])

plt.subplot(141)
plt.imshow(h, cmap="gray")
plt.title("H Channel - hue")

plt.subplot(142)
plt.imshow(s, cmap="gray")
plt.title("S Channel - saturation")

plt.subplot(143)
plt.imshow(v, cmap="gray")
plt.title("V Channel - value")

# Show the merged output
plt.subplot(144)
plt.imshow(img_NZ_rgb)
plt.title("Original")

plt.show()
