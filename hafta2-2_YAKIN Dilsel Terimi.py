
"""
Hafta 2 - Sayfa 38
Ödev-2 (Odev2.py): Yukarıda verilen mesafe dilsel değişkenine ait 
YAKIN dilsel teriminin bulanık kümesinin [-500, 500] evrensel kümesi 
için çizen Python kodunu yazınız?

"""

import matplotlib.pyplot as plt
import numpy as np

# Mesafe dilsel değişkeni ve üyelik fonksiyonları
def very_near_membership(distance):
    if distance < 200:
        return 1
    elif 200 <= distance <= 500:
        return (500 - distance) / 300
    else:
        return 0

# Evrensel küme için mesafe değerleri
distances = np.linspace(-500, 500, 1000)

# Üyelik derecelerini hesapla
membership_values = [very_near_membership(distance) for distance in distances]

# Grafik çizimi
plt.plot(distances, membership_values, label='YAKIN Dilsel Terimi')
plt.title('YAKIN Dilsel Terimi Bulanık Kümesi')
plt.xlabel('Mesafe')
plt.ylabel('Üyelik Derecesi')
plt.legend()
plt.grid(True)
plt.show()
