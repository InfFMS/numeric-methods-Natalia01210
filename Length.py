#R = U/I
import matplotlib.pyplot as plt
import numpy as np

with open('data.csv', encoding="utf-8") as f:
    e = f.readlines()
print(e)
mI, mU = [] , []
for i in range(len(e)-1):
    a, b = e[i+1].split(',')
    mI.append(float(a))
    mU.append(float(b[:-1]))
m = []
for i in range(len(mI)):
    m.append(mU[i] / mI[i])

l = min(m)
r = max(m)
i = l
q = []
p = []
while(i <= r):
    sum = 0
    for k in range(len(mI)):
        sum += (i*mI[k] - mU[k])**2
    q.append(sum)
    p.append(mU[k]/mI[k])
    i +=0.01
print("Cопротивление резистора:", p[q.index(min(q))])
fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(1, 1, 1)
plt.scatter(mI, mU)
plt.show()