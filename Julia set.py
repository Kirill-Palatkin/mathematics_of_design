import random
import numpy as np
import matplotlib.pyplot as plt


def julia_set(c, width, height, zoom=1, max_iter=100):
    x = np.linspace(-2 / zoom, 2 / zoom, width)
    y = np.linspace(-2 / zoom, 2 / zoom, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    img = np.zeros(Z.shape, dtype=int)

    for n in range(max_iter):
        mask = np.abs(Z) < 2
        img[mask] = n
        Z[mask] = Z[mask]**2 + c

    img[img == max_iter - 1] = 0

    return img


constants = [-0.8 + 0.156j, -0.4 + 0.6j, 0.285 + 0.01j, -0.70176 - 0.3842j, -0.835 - 0.2321j,
             0.355534 - 0.337292j, -0.123 + 0.745j, -0.75 + 0.11j, 0.285 + 0.013j, -0.74543 + 0.11301j]

width, height = 800, 800
zoom = 1
max_iter = int(input('Кол-во итераций: '))

img = julia_set(random.choice(constants), width, height, zoom, max_iter)

plt.figure(figsize=(8, 8))
plt.imshow(img, extent=(-2 / zoom, 2 / zoom, -2 / zoom, 2 / zoom), cmap=random.choice(['hot', 'viridis', 'plasma', 'inferno', 'magma', 'hot', 'cool', 'gray']))
plt.title(f'c = {random.choice(constants)}, {max_iter} итераций')
plt.axis('off')
plt.show()
