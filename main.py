import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


fig, ax = plt.subplots()
fig.figsize = (10, 10)
N_iteration_max = 50
N_points = int(500)
x_min, x_max, y_min, y_max = -2, 1, -1, 1
hx, hy = (x_max - x_min)/N_points, (y_max - y_min)/N_points


def is_convergent(a, b):
    xn, yn = 0, 0
    xn1, yn1 = 0, 0
    k = 0
    while xn1*xn1+yn1*yn1 <= 4 and k < N_iteration_max:
        xn1 = xn*xn-yn*yn+a
        yn1 = 2*xn*yn+b
        k += 1
        xn, yn = xn1, yn1

    if k != N_iteration_max:
        return 1-k/N_iteration_max
    else:
        return 0


def get_color(coefficient):
    if coefficient == 0:
        return 0, 0, 0
    else:
        coefficient *= N_iteration_max
        r, g, b = 3*coefficient % 256, 1*coefficient % 256, 10*coefficient % 256
        r /= 255
        g /= 255
        b /= 255
        return 1-r, 1-g, 1-b


if __name__ == '__main__':
    for i in tqdm(range(N_points)):
        for j in range(N_points):
            x = x_min + i * hx
            y = y_min + j * hy
            c = is_convergent(x, y)
            color = get_color(c)
            ax.plot([x], [y], color=color, linewidth=0, marker=",")
    plt.savefig("mandelbrot.pdf")
    plt.show()

