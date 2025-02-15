import matplotlib.pyplot as plt
import numpy as np

def F(n1, n2, ax, ay, bx, by):
    x = np.linspace(ax, bx, 100)
    y = n1 * ((ay ** 2 + (x - ax) ** 2)** 0.5) + n2 * ((by ** 2 + (x - bx) ** 2)** 0.5)
    a, b = ax, bx
    while(a - b > 0.01):
        i
    fig = plt.figure(figsize=(14, 6))
    ax = plt.subplot(1, 1, 1)
    plt.plot(x, y)
    plt.show()
n1, n2 = 1, 1
ax, ay, = 0, 1
bx, by = 1, -1
F(n1, n2, ax, ay, bx, by)