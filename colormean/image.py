import cv2
import statistics


class Image:

    def __init__(self, file_name: str):
        self.img = cv2.imread(file_name)
        self.row_count = self.img.shape[0]
        self.column_count = self.img.shape[1]
        self.section_row_divides = [0]
        self.section_column_divides = [0]
        self.section_array = []

    def set_bgr(self, row: int, col: int, b: int, g: int, r: int):
        self.set_blue(row, col, b)
        self.set_green(row, col, g)
        self.set_red(row, col, r)

    def set_blue(self, row: int, col: int, b: int):
        self.img.itemset((row, col, 0), b)

    def set_green(self, row: int, col: int, g: int):
        self.img.itemset((row, col, 1), g)

    def set_red(self, row: int, col: int, r: int):
        self.img.itemset((row, col, 2), r)

    def get_blue(self, row: int, col: int):
        return self.img.item(row, col, 0)

    def get_green(self, row: int, col: int):
        return self.img.item(row, col, 1)

    def get_red(self, row: int, col: int):
        return self.img.item(row, col, 2)

    def get_bgr(self, row: int, col: int):
        return [self.get_blue(row, col), self.get_green(row, col), self.get_red(row, col)]

    def save(self, new_file_name: str):
        cv2.imwrite(new_file_name, self.img)

    def gen_sections(self, rows: int, cols: int):
        for x in range(1, rows + 1):
            end = int((x / rows) * self.row_count)
            self.section_row_divides.append(end)
        for x in range(1, cols + 1):
            end = int((x / cols) * self.column_count)
            self.section_column_divides.append(end)

    def gen_mean_pic(self, rows: int, cols: int):
        self.gen_sections(rows, cols)
        for x in range(len(self.section_row_divides) - 1):
            for y in range(len(self.section_column_divides) - 1):
                self.section_array.append(Section(self.section_row_divides[x], self.section_row_divides[x + 1],
                                                  self.section_column_divides[y], self.section_column_divides[y + 1], self))
        for section in self.section_array:
            section : Section
            section.set_color_to_avg()


    def print_sections(self):
        for x in self.section_array:
            print(x)


class Section:

    def __init__(self, start_row: int, end_row: int, start_col: int, end_col: int, image : Image):
        self.img = image
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col
        self.avg_blue = 0
        self.avg_green = 0
        self.avg_red = 0

    def calc_average_color(self):
        blue_list = []
        green_list = []
        red_list = []
        for row in range(self.start_row, self.end_row):
            for col in range(self.start_col, self.end_col):
                bgr = self.img.get_bgr(row, col)
                blue_list.append(bgr[0] ** 2)
                green_list.append(bgr[1] ** 2)
                red_list.append(bgr[2] ** 2)
        self.avg_blue = int(statistics.mean(blue_list) ** 0.5)
        self.avg_green = int(statistics.mean(green_list) ** 0.5)
        self.avg_red = int(statistics.mean(red_list) ** 0.5)

    def set_color(self, b : int, g : int, r : int):
        for row in range(self.start_row, self.end_row):
            for col in range(self.start_col, self.end_col):
                self.img.set_bgr(row, col, b, g, r)

    def set_color_to_avg(self):
        self.calc_average_color()
        self.set_color(self.avg_blue, self.avg_green, self.avg_red)

    def __str__(self):
        return "rows: " + str(self.start_row) + " to " + str(self.end_row) + " cols: " + str(
            self.start_col) + " to " + str(self.end_col)
