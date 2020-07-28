import cv2
from image import Image


def make_mean_pic(rows : int, columns : int, img_file_name : str):
    pic = Image(img_file_name)
    # for row in range(pic.img.shape[0]):
    #     for column in range(pic.img.shape[1]):
    #         pic.set_bgr(row, column, 0, 0, 0)
    for x in range(1, rows):
        print(x)





def format_color(bgr : list) -> str:
    return 'blue ' + str(bgr[0]) + " green " + str(bgr[1]) + ' red ' + str(bgr[2])

make_mean_pic(2, 1, "img/quadrants.jpg")
