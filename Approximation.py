import matplotlib.pyplot as plt
import numpy as np

#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0

print("Решение уравнения x³ - x + 1 = 0:")
def f(x):
    return x ** 3 - x + 1
l = -2
r = -1
while(r - l >= 0.0001):
    if(f(l + (r-l)/2) > 0):
        r = l + (r-l)/2
    else:
        l = l + (r-l)/2
print(round(l, 2))
x = np.linspace(-3, 3, 100)
y = x ** 3 - x + 1
fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(2, 3, 1)
plt.plot(x, y)
ax.plot([-3, 3],[0, 0])
plt.title("y = x³ - x + 1")
plt.grid()

print("Решение уравнения x³ - x² - 9x + 9 = 0:")
def f(x):
    return x ** 3 - x ** 2 - 9 * x + 9
l = -4
r = -2
while(r - l >= 0.0001):
    if(f(l + (r-l)/2) > 0):
        r = l + (r-l)/2
    else:
        l = l + (r-l)/2
print(round(l, 2))
l = 0
r = 2
while(r - l >= 0.0001):
    if(f(r - (r-l)/2) > 0):
        l = r - (r-l)/2
    else:
        r = r - (r-l)/2
print(round(l, 2))
l = 2
r = 4
while(r - l >= 0.0001):
    if(f(l + (r-l)/2) > 0):
        r = l + (r-l)/2
    else:
        l = l + (r-l)/2
print(round(l, 2))
x = np.linspace(-4, 4, 100)
y = x ** 3 - x ** 2 - 9 * x + 9
ax = plt.subplot(2, 3, 2)
plt.plot(x, y)
ax.plot([-4, 4],[0, 0])
plt.title("y = x³ - x² - 9x + 9")
plt.grid()

print("Решение уравнения x² - eᵡ = 0:")
def f(x):
    return x ** 2 - np.e ** x
l = -2
r = 2
while(r - l >= 0.0001):
    if(f(r - (r-l)/2) > 0):
        l = r - (r-l)/2
    else:
        r = r - (r-l)/2
print(round(l, 2))
x = np.linspace(-2, 2, 100)
y = x ** 2 - np.e ** x
ax = plt.subplot(2, 3, 3)
plt.plot(x, y)
ax.plot([-2, 2],[0, 0])
plt.title("y = x² - eᵡ")
plt.grid()

print("Решение уравнения 5x - 6ln(x) - 7 = 0:")
def f(x):
    return 5 * x - 6 * np.log(x) - 7
l = 0.0001
r = 1
while(r - l >= 0.0001):
    if(f(r - (r-l)/2) > 0):
        l = r - (r-l)/2
    else:
        r = r - (r-l)/2
print(round(l, 2))
l = 1
r = 4
while(r - l >= 0.0001):
    if(f(l + (r-l)/2) > 0):
        r = l + (r-l)/2
    else:
        l = l + (r-l)/2
print(round(l, 2))
x = np.linspace(0.0001, 4, 100)
y = 5 * x - 6 * np.log(x) - 7
ax = plt.subplot(2, 3, 4)
plt.plot(x, y)
ax.plot([0.0001, 4],[0, 0])
plt.title("y = 5x - 6ln(x) - 7")
plt.grid()

print("Решение уравнения cos(x) + 2x – 3 = 0:")
def f(x):
    return np.cos(x) + 2 * x - 3
l = 0
r = 4
while(r - l >= 0.0001):
    if(f(l + (r-l)/2) > 0):
        r = l + (r-l)/2
    else:
        l = l + (r-l)/2
print(round(l, 2))
x = np.linspace(0, 4, 100)
y = np.cos(x) + 2 * x - 3
ax = plt.subplot(2, 3, 5)
plt.plot(x, y)
ax.plot([0, 4],[0, 0])
plt.title("y = cos(x) + 2x – 3")
plt.grid()

plt.tight_layout()
plt.show()