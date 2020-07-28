import cv2


def make_mean_pic(rows : int, columns : int, img_file_name : str):
    img = cv2.imread(img_file_name)
    print(type(img))

    # for row in range(img.shape[0]):
    #     for column in range(img.shape[1]):
    #         img[row, column] = [0, 0, 0]

    # cv2.imwrite("quadrants-new.jpg", img)




def format_color(bgr : list) -> str:
    return 'blue ' + str(bgr[0]) + " green " + str(bgr[1]) + ' red ' + str(bgr[2])

make_mean_pic(1, 1, "img/quadrants.jpg")
