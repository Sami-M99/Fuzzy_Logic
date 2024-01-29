"""
Hafta2 - Sayfa 55
Yamuk Üyelik Fonksiyonu
Üyelik Dereceleri ve Üyelik Fonksiyonları
Cevap sayfa 51 ile bağlıdır
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.arange(1,100,1)
x_pi=[]
b_genislik=20
ilk_orta_nokta=40
ikinci_orta_nokta=60

t=[]
a=ilk_orta_nokta - b_genislik
b=ilk_orta_nokta
c=ikinci_orta_nokta
d=ikinci_orta_nokta + b_genislik



def pi_ciz(a,b,c):
    for i,u in enumerate(x):
        if(u<a): t.insert(i, 0)
        if(a<=u and u<b): t.insert(i,((u-a)/(b-a)))
        if(b<=u and u<=c): t.insert(i, 1)
        if(c<u and u<=d): t.insert(i,((d-u)/(d-c)))                
        if(u>d): t.insert(i, 0)
        x_pi.append(u)



u=float(input("1-100 arasında değer girin:"))
if(u<a):mx= 0
if(a<=u and u<b): mx= ((u-a)/(b-a))
if(b<=u and u<=c): mx= 1
if(c<u and u<=d): mx= ((d-u)/(d-c))
if(u>d): mx= 0
print("üyelik derecesi: ",mx)

x1,y1=[u,u],[0,mx]
x2,y2=[u,0],[mx,mx]

pi_ciz(a, b, c)          
plt.plot(x_pi,t, color="black")
plt.plot(x1,y1,marker="o",color="red")
plt.plot(x2,y2, marker="o",color="red") 
