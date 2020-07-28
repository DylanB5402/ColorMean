import cv2

class Image:

    def __init__(self, file_name : str):
        self.img = cv2.imread(file_name)
        self.row_count = self.img.shape[0]
        self.column_count = self.img.shape[1]

    def set_bgr(self, row : int, col : int, b : int, g : int, r : int):
        self.set_blue(row, col, b)
        self.set_green(row, col, g)
        self.set_red(row, col, r)

    def set_blue(self, row : int, col : int, b : int):
        self.img.itemset((row, col, 0), b)

    def set_green(self, row : int, col : int, g : int):
        self.img.itemset((row, col, 1), g)

    def set_red(self, row : int, col : int, r : int):
        self.img.itemset((row, col, 2), r)

    def save(self, new_file_name : str):
        cv2.imwrite(new_file_name, self.img)