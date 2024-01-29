"""
Hafta2 - Sayfa 85
t-conorm & tNorm

Ödev-5
Girişler: Sıcaklık
Evrensel Küme: np.arange(20,81,1)
Low:[20,25,35,40]
Medium:[30,42,55,80]
Yukarıdaki bilgilere göre Low ve Med bulanık kümelerinin Birleşimini ve kesişimini tüm t-norm ve s-norm yöntemlerine göre hesaplayıp görselleştiren Python programını yazın. Bu ödev cevabı öğrencilerle paylaşılmayacaktır. Her öğrenci kendisi yapacaktır.

Cevap sayfa 81 + 82 ile bağlıdır
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20, 81, 1)
a = []   # Medium
b = []   # Low
bi = []


# # ----- t-conorm  |  S-norm  ----- 

#  tConorm Maksimum
def tConormMax():
    for i, c in enumerate(x):
        bi.insert(i, max(a[i], b[i]))

# tConorm Cebirsel Toplam (Algebric Sum)
def tConormCebirselToplam():
    for i, c in enumerate(x):
        bi.insert(i, ((a[i] + b[i]) - (a[i] * b[i])))
        
# tConorm Sınırlı Toplam (Bounded sum)
def tConormSınırlıToplam():
    for i, c in enumerate(x):
        bi.insert(i, min(1, a[i] + b[i]))

# tConorm Güçlü Toplam (Drastic sum) 
def tConormGüçlüToplam():
    for i, c in enumerate(x):
        if (a[i] == 0):
            bi.insert(i, b[i])
        elif (b[i] == 0):
            bi.insert(i, a[i])
        elif (a[i] > 0 and b[i] > 0):
            bi.insert(i, 1)

# # -------- tNorm  -------- 

# tNorm Minimum
def tNormMin():
    for i, c in enumerate(x):
        bi.insert(i, min(a[i], b[i]))

# tNorm Cebirsel Çarpım (Algebric product)
def tNormCebirselÇarpım():
    for i, c in enumerate(x):
        bi.insert(i, a[i] * b[i])

# tNorm Sınırlı Çarpım (Bounded product)
def tNormSınırlıÇarpım():
    for i, c in enumerate(x):
        bi.insert(i, max(0, a[i] + b[i] - 1))
        

# Güçlü Çarpım (Drastic product)
def tCnormGüçlüÇarpım():
    for i, c in enumerate(x):
        if (a[i] == 1):
            bi.insert(i, b[i])
        elif (b[i] == 1):
            bi.insert(i, a[i])
        elif (a[i] < 1 and b[i] < 1):
            bi.insert(i, 0)


# # -------- Low ve Medium çizimi -------- 
for i, u in enumerate(x):
    if (u == 20):
        b.insert(i, 0)
    elif (20 < u and u <= 25):
        b.insert(i, (u - 20) / 5)
    elif (25 < u and u <= 35):
        b.insert(i, 1)
    elif (35 < u and u <= 40):
        b.insert(i, (40 - u) * 0.2)
    else:
        b.insert(i, 0)

for i, m in enumerate(x):
    if (m < 30):
        a.insert(i, 0)
    elif (30 <= m and m <= 42):
        a.insert(i, (m - 30) / 12)
    elif (42 < m and m <= 55):
        a.insert(i, 1)
    elif (55 < m and m <= 80):
        a.insert(i, (80 - m) * 0.04)


# # -------- Grafikler -------- 
plt.figure(figsize=(10, 8))

plt.subplot(4, 2, 1)
tConormMax()
plt.plot(x, bi, color="orange")
plt.title("tConorm Maksimum")

plt.subplot(4, 2, 2)
bi = []  # Clear the previous values
tConormCebirselToplam()
plt.plot(x, bi, color="blue")
plt.title("tConorm Cebirsel Toplam")

plt.subplot(4, 2, 3)
bi = []  # Clear the previous values
tConormSınırlıToplam()
plt.plot(x, bi, color="green")
plt.title("tConorm Sınırlı Toplam")

plt.subplot(4, 2, 4)
bi = []  # Clear the previous values
tConormGüçlüToplam()
plt.plot(x, bi, color="red")
plt.title("tConorm Güçlü Toplam")

#----------------------

plt.subplot(4, 2, 5)
bi = []  # Clear the previous values
tNormMin()
plt.plot(x, bi, color="purple")
plt.title("tNorm Minimum")

plt.subplot(4, 2, 6)
bi = []  # Clear the previous values
tNormCebirselÇarpım()
plt.plot(x, bi, color="pink")
plt.title("tNorm Cebirsel Çarpım")

plt.subplot(4, 2, 7)
bi = []  # Clear the previous values
tNormSınırlıÇarpım()
plt.plot(x, bi, color="pink")
plt.title("tNorm Sınırlı Çarpım")

plt.subplot(4, 2, 8)
bi = []  # Clear the previous values
tCnormGüçlüÇarpım()
plt.plot(x, bi, color="pink")
plt.title("tNorm Güçlü Çarpım")

plt.tight_layout()
plt.show()
