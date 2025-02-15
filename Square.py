import matplotlib.pyplot as plt
import numpy as np

def F(l, r):
    i = l
    sq = 0
    while(i < r):
        #sq += (abs(f1(i) - f2(i)) + abs(f1(i+0.001) - f2(i+0.001)))/2*0.001
        #sq += abs(f1(i) - f2(i))*0.001
        sq += abs(f1((i + 0.001) / 2) - f2((i + 0.001)/2))*0.001
        rect = plt.Rectangle((i, min(f1(i), f2(i))), 0.001, abs(f1(i) - f2(i)), color="blue", alpha=0.5)
        ax.add_patch(rect)
        i += 0.001
    return sq


def f1(x):
 return np.sin(2*x) + 1
def f2(x):
 return -0.2 * x ** 2 + 0.5
x = np.linspace(0, np.pi, 100)
y = f1(x)
b = f2(x)

fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(2, 3, 1)
plt.plot(x, y, color='black')
plt.plot(x, b, color='black')
plt.plot([0, 0], [y[0], b[0]], color='black')
plt.plot([np.pi, np.pi], [y[-1], b[-1]], color='black')
print(F(0, np.pi))


def f1(x):
 return np.cos(x) + 1.2
def f2(x):
 return -0.5 * x ** 2 + 0.7
x = np.linspace(-np.pi/2, np.pi/2, 100)
y = f1(x)
b = f2(x)

ax = plt.subplot(2, 3, 2)
plt.plot(x, y, color='black')
plt.plot(x, b, color='black')
plt.plot([-np.pi/2, -np.pi/2], [y[0], b[0]], color='black')
plt.plot([np.pi/2, np.pi/2], [y[-1], b[-1]], color='black')
print(F(-np.pi/2, np.pi/2))


def f1(x):
 return np.e ** (-1 * x ** 2) + 1
def f2(x):
 return -0.3 * x ** 3 + 0.5
x = np.linspace(-2, 2, 100)
y = f1(x)
b = f2(x)

ax = plt.subplot(2, 3, 3)
plt.plot(x, y, color='black')
plt.plot(x, b, color='black')
plt.plot([-2, -2], [y[0], b[0]], color='black')
plt.plot([2, 2], [y[-1], b[-1]], color='black')
print(F(-2, 2))


def f1(x):
 return np.e ** (-1 * x ** 2) + 0.5
def f2(x):
 return 0.2 * np.sin(3 * x) - 0.5
x = np.linspace(-2, 2, 100)
y = f1(x)
b = f2(x)

ax = plt.subplot(2, 3, 4)
plt.plot(x, y, color='black')
plt.plot(x, b, color='black')
plt.plot([-2, -2], [y[0], b[0]], color='black')
plt.plot([2, 2], [y[-1], b[-1]], color='black')
print(F(-2, 2))


def f1(x):
 return np.e ** (-1 * (x + 1) ** 2) + np.e ** (-1 * (x - 1) ** 2) + 0.5
def f2(x):
 return -1 * 0.3 * x ** 2
x = np.linspace(-2, 2, 100)
y = f1(x)
b = f2(x)

ax = plt.subplot(2, 3, 5)
plt.plot(x, y, color='black')
plt.plot(x, b, color='black')
plt.plot([-2, -2], [y[0], b[0]], color='black')
plt.plot([2, 2], [y[-1], b[-1]], color='black')
print(F(-2, 2))


plt.show()