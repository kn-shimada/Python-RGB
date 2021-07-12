# Copyright (c) 2021 kn-shimada
# 最頻値

import numpy as np
import PIL.ImageDraw
import scipy.stats as stats

source_file = 'sample_picture.jpg'
source = PIL.Image.open(source_file)

small_img = source.resize((100, 100))
color_arr = np.array(small_img)
w_size, h_size, n_color = color_arr.shape
color_arr = color_arr.reshape(w_size * h_size, n_color)

color_mode, _ = stats.mode(color_arr, axis=0)
color_mode = tuple(color_mode[0])

im = PIL.Image.new('RGB', (100, 100), color_mode)
im.save('result_02.png')