"""
Hafta2 - Sayfa 55
Üçgen Üyelik Fonksiyonu
Üyelik Dereceleri ve Üyelik Fonksiyonları
Cevap sayfa 49 ile bağlıdır
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.arange(1,100,1)

b_genislik=40
b_orta_nokta=50

t=[]
a=b_orta_nokta-b_genislik
b=b_orta_nokta
c=b_orta_nokta+b_genislik


## grafik için
def pi_ciz(a,b,c):
    for i,u in enumerate(x):
        if(u<a): t.insert(i, 0)
        if(u>=a and u<=b): t.insert(i,((u-a)/(b-a)))
        if(u>b and u<=c): t.insert(i,((c-u)/(c-b)))                
        if(u>c): t.insert(i, 0)


## noktalar için
u=float(input("1-100 arasında değer girin:"))
if(u<a):mx=0
if(u>=a and u<=b): mx=((u-a)/(b-a))
if(u>b and u<=c):mx= ((c-u)/(c-b))
print("üyelik derecesi: ",mx)

x1,y1=[u,u],[0,mx]
x2,y2=[u,0],[mx,mx]

pi_ciz(a, b, c)          
plt.plot(x,t, color="black")
plt.plot(x1,y1,marker="o",color="red")
plt.plot(x2,y2, marker="o",color="red") 