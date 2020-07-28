import cv2

class Image:

    def __init__(self, file_name : str):
        self.img_array = cv2.imread(file_name)

    def set_bgr(self, row : int, col : int, b : int, g : int, r : int):
        self.set_blue(row, col, b)
        self.set_green(row, col, g)
        self.set_red(row, col, r)

    def set_blue(self, row : int, col : int, b : int):
        self.img_array.itemset((row, col, 0), b)

    def set_green(self, row : int, col : int, g : int):
        self.img_array.itemset((row, col, 1), g)

    def set_red(self, row : int, col : int, r : int):
        self.img_array.itemset((row, col, 2), r)

    def save(self, new_file_name : str):
        cv2.imwrite(new_file_name, self.img_array)