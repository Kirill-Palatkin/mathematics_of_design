import random

import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    img = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            img[j, i] = mandelbrot(x[i] + 1j * y[j], max_iter)

    return img


width, height = 400, 400
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = int(input('Кол-во итераций: '))

img = create_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

plt.imshow(img, extent=(x_min, x_max, y_min, y_max), cmap=random.choice(['hot', 'viridis', 'plasma', 'inferno', 'magma', 'hot', 'cool', 'gray']))
plt.xticks([])
plt.yticks([])
plt.show()
