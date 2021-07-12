# Copyright (c) 2021 kn-shimada
# 平均

import numpy as np
import PIL.ImageDraw

source_file = 'sample_picture.jpg'
source = PIL.Image.open(source_file)

small_img = source.resize((100, 100))
color_arr = np.array(small_img)
w_size, h_size, n_color = color_arr.shape
color_arr = color_arr.reshape(w_size * h_size, n_color)

color_mean = np.mean(color_arr, axis=0)
color_mean = color_mean.astype(int)
color_mean = tuple(color_mean)

im = PIL.Image.new('RGB', (100, 100), color_mean)
im.save('result_01.png')