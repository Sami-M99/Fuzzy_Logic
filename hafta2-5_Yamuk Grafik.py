
"""
Hafta2 - Sayfa 85

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20, 81, 1)
a = []   # Medium
b = []   # Low


# Define membership functions for a and b
for u in x:
    if 20 <= u <= 25:
        b.append((u - 20) / 5)
    elif 25 < u <= 35:
        b.append(1)
    elif 35 < u <= 40:
        b.append((40 - u) /5)
    else:
        b.append(0)


for m in x:
    if m < 30:
        a.append(0)
    elif 30 <= m <= 42:
        a.append((m - 30) / 12)
    elif 42 < m <= 55:
        a.append(1)
    elif 55 < m <= 80:
        a.append((80 - m) /25)


# Plot the membership functions
plt.plot(x, b, color="blue", label="Low")
plt.plot(x, a, color="orange", label="Medium")
plt.legend()
plt.xlabel("Sıcaklık")
plt.ylabel("Membership")
plt.title("Membership Functions")
plt.grid(True)
plt.show()
