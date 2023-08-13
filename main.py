import os

from zipfile import ZipFile
from urllib.request import urlretrieve

from PIL import Image


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

image_checkerboard18x18 = Image.open("checkerboard_18x18.png")
image_checkerboard18x18.show()

image_checkerboard84x84 = Image.open("checkerboard_84x84.jpg")
image_checkerboard84x84.show()

