#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.cos(x)
x = 0
y = f(x)
sum = 0
while(x <= np.pi):
    sum += ((0.0001)**2 + abs(f(x+0.0001) - f(x))**2) ** 0.5
    x += 0.0001
    y = f(x+0.0001)
print(sum)
x = np.linspace(0, np.pi, 100)
y = np.cos(x)
fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(2, 2, 1)
plt.plot(x, y)
ax.plot([0, np.pi],[0, 0])



plt.show()
