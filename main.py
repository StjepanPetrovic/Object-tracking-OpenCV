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

img = cv2.imread("checkerboard_18x18.png", cv2.IMREAD_GRAYSCALE)

# if this is not converted, BGR color space is there and therefor image is yellow and purple
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img, cmap="gray")
plt.show()

img_copy = img.copy()
img_copy[2, 2] = 200
img_copy[2, 3] = 200
img_copy[3, 2] = 200
img_copy[3, 3] = 200

# Same as above
# img_copy[2:3,2:3] = 200

plt.imshow(img_copy, cmap="gray")
plt.show()
print(img_copy)
