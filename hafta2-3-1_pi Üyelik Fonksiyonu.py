"""
Hafta2 - Sayfa 55
Üyelik Dereceleri ve Üyelik Fonksiyonları -> piUyelikFonksiyonu.py
Cevap sayfa 52 + 53 ile bağlıdır
"""


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,100,1)
x_pi=[]
b_genislik=40
c_orta_nokta=50

t=[]
a=c_orta_nokta-b_genislik
b=c_orta_nokta-b_genislik/2
c=c_orta_nokta
d=c_orta_nokta+b_genislik/2
e=c_orta_nokta+b_genislik


# grafik için
def pi_ciz(a,b,c,d,e):
    for i,u in enumerate(x):
        if(u<=c):
            if(u<a): t.insert(i, 0)
            elif(u>=a and u<=b): t.insert(i,2*(pow(((u-a)/(c-a)),2)))
            elif(u>b and u<=c): t.insert(i,1-2*(pow(((u-c)/(c-a)),2)))                
            elif(u>c): t.insert(i, 1)
        if(u>c):
            if(u<c): t.insert(i, 1)  
            elif(u>=c and u<=d): t.insert(i,1-2*(pow(((u-c)/(e-c)),2)))                  
            elif(u>d and u<=e): t.insert(i,1-(1-2*(pow(((u-e)/(e-c)),2))))                 
            elif(u>e): t.insert(i, 0) 
        x_pi.append(u)


# noktalar için
cevap = 'e'   
while(cevap.lower() =='e'):
        u=float(input("1-100 arasında değer girin:"))
        if(u<a):mx=0
        if(a<=u and u<=b): mx=2*(pow(((u-a)/(c-a)),2))
        if(b<u and u<=c):mx= 1-2*(pow(((u-c)/(c-a)),2))
        if(c<u and u<=d):mx=1-2*(pow(((u-c)/(e-c)),2))
        if(d<u and u<=e):mx=1-(1-2*(pow(((u-e)/(e-c)),2)))
        print("üyelik derecesi: ",mx)
        cevap=input("Devam edecek misiniz (E/e)?")
        
        x1,y1=[u,u],[0,mx]
        x2,y2=[u,0],[mx,mx]
        
        pi_ciz(a, b, c, d, e)          
        plt.plot(x_pi,t, color="black")
        plt.plot(x1,y1,marker="o",color="red")
        plt.plot(x2,y2, marker="o",color="red") 

plt.show()









