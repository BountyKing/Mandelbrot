import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

step = 0.001


def f(i):
    theta = i*step
    return np.cos(theta)+np.cos(np.pi*theta), np.sin(theta)+np.sin(np.pi*theta)


if __name__ == '__main__':
    print("Starting")
    X, Y = [], []
    fig, ax = plt.subplots()
    # anim = FuncAnimation(fig, func=f, frames=np.arange(1000))
    X, Y = f(3)
    ax.plot(X, Y)
    plt.show()


