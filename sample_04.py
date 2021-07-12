# 中央値

import numpy as np
import PIL.ImageDraw

source_file = 'sample_picture.jpg'
source = PIL.Image.open(source_file)

small_img = source.resize((100, 100))
color_arr = np.array(small_img)
w_size, h_size, n_color = color_arr.shape
color_arr = color_arr.reshape(w_size * h_size, n_color)
r = [elem[0] for elem in color_arr]
g = [elem[1] for elem in color_arr]
b = [elem[2] for elem in color_arr]
color_median = (int(np.median(r)), int(np.median(g)), int(np.median(b)))

im = PIL.Image.new('RGB', (100, 100), color_median)
im.save('result_04.png')