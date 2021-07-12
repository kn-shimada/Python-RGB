# 画像中の最頻値

import numpy as np
import PIL.ImageDraw
import scipy.stats

source_file = 'sample_picture.jpg'
source = PIL.Image.open(source_file)

small_img = source.resize((100, 100))
color_arr = np.array(small_img)
w_size, h_size, n_color = color_arr.shape
color_arr = color_arr.reshape(w_size * h_size, n_color)
color_code = ['{:02x}{:02x}{:02x}'.format(*elem) for elem in color_arr]
mode, _ = scipy.stats.mode(color_code)
r = int(mode[0][0:2], 16)
g = int(mode[0][2:4], 16)
b = int(mode[0][4:6], 16)
color_mode = (r, g, b)

im = PIL.Image.new('RGB', (100, 100), color_mode)
im.save('result_03.png')