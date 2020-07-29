import cv2

class Image:

    def __init__(self, file_name : str):
        self.img = cv2.imread(file_name)
        self.row_count = self.img.shape[0]
        self.column_count = self.img.shape[1]
        self.section_row_divides = [0]
        self.section_column_divides = [0]
        self.section_array = []

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

    def gen_sections(self, rows : int, cols : int):
        # start: int = 0
        for x in range(1, rows + 1):
            end = int((x / rows) * self.row_count)
            self.section_row_divides.append(end)
        for x in range(1, cols + 1):
            end = int((x / cols) * self.column_count)
            self.section_column_divides.append(end)
        # print(self.section_row_divides)
        # print(self.section_column_divides)

    def gen_mean_pic(self, rows : int, cols : int):
        self.gen_sections(rows, cols)
        for x in range(len(self.section_row_divides) - 1):
            print(x)
            for y in range(self.section_row_divides[x], self.section_row_divides[x+1]):
                for z in range(len(self.section_column_divides) - 1):
                    print(self.section_row_divides[z])


class Section:

    def __init__(self, start_row : int, end_row : int, start_col : int, end_col : int):
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col

    def get_average_color(self, img : Image):
        pass
