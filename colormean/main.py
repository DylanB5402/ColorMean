from image import Image

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html


def format_color(bgr : list) -> str:
    return 'blue ' + str(bgr[0]) + " green " + str(bgr[1]) + ' red ' + str(bgr[2])


quadrants = Image("img/pua.png")
quadrants.gen_mean_pic(50, 50)
quadrants.save("pic.jpg")
