""" 
Hafta4 - Sayfa 28
Mamdani and Larsen

ödev-6:
Çıkış: Sıcaklık
Evrensel Küme: np.arange(20,81,1)
Low:[20,25,35,40]
Medium:[30,42,55,80]
Kural 1: Öncül çıkışı:0.4 (Low->22)
Çıkış Kümesi: Low olacak şekilde mamdani’ye göre çıkış kümesini elde edip görselleştirin.
Kural 2: Öncül Çıkışı:0.75 (Med->39)
Çıkış Kümesi:Med olacak şekilde mamdaniye göre çıkış kümesini elde edip görselleştirin.
Yukarıdaki benzer işlemleri Larsen’e göre de gerçekleştirip ayrı bir görsel olarak çizdirin.

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20, 81, 1)
a = []   # Medium
b = []   # Low

# Initialize x_sol and x_sag lists
low = []
medium = []

mamdaniLow =[]
mamdaniMedium =[]
mamdaniMax = []

larsenLow =[]
larsenMedium =[]
larsenMax=[]

# Define membership functions for a and b
for u in x:
    if 20 <= u <= 25:
        b.append((u - 20) / 5)
    elif 25 < u <= 35:
        b.append(1)
    elif 35 < u <= 40:
        b.append((40 - u) * 0.2)
    else:
        b.append(0)
    low.append(u)

for m in x:
    if m < 30:
        a.append(0)
    elif 30 <= m <= 42:
        a.append((m - 30) / 12)
    elif 42 < m <= 55:
        a.append(1)
    elif 55 < m <= 80:
        a.append((80 - m) * 0.04)
    medium.append(m)
    
    
    
def mamdani():
    for i,c in enumerate(x):
          mamdaniLow.insert(i, min(0.4,b[i]))
          mamdaniMedium.insert(i, min(0.75,a[i]))
          mamdaniMax.append(max(mamdaniLow[i],mamdaniMedium[i]))

def larsen():
    for i,c in enumerate(x):
          larsenLow.insert(i, 0.4*b[i])
          larsenMedium.insert(i, 0.75*a[i])
          larsenMax.insert(i, max(larsenLow[i],larsenMedium[i]))

mamdani()
larsen()

# Plot the membership functions
plt.figure(figsize=(8,4))

plt.subplot(2, 2, 1)
plt.plot(low, b, color="blue")
plt.plot(medium, a, color="orange")
plt.fill_between(x,mamdaniLow, color="yellow",alpha=1)
plt.fill_between(x,mamdaniMedium, color="pink",alpha=1)


plt.subplot(2, 2, 2)
plt.fill_between(x,mamdaniMax, color="green")

plt.subplot(2, 2, 3)
plt.plot(low, b, color="blue")
plt.plot(medium, a, color="orange")
plt.fill_between(x,larsenLow, color="yellow")
plt.fill_between(x,larsenMedium, color="pink")

plt.subplot(2, 2, 4)
plt.fill_between(x, larsenMax, color="orange")

plt.show()