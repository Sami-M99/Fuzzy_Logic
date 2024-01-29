"""
Hafta2 - Sayfa 79
Üyelik Fonksiyonlarını Değiştiren Bulanık Küme İşlemleri
Cevap sayfa 77 + 78 ile bağlıdır

Ödev-4: PI bulanık kümesine aşağıdaki işlemleri uygulayan yazılımı geliştirin?
a-) Kuvvet
b-) Derişme
c-) Genişleme
d-) Yoğunlaşma

"""


import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,100,1)

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
            if(u>=a and u<=b): t.insert(i,2*(pow(((u-a)/(c-a)),2)))
            if(u>b and u<=c): t.insert(i,1-2*(pow(((u-c)/(c-a)),2)))                
            if(u>c): t.insert(i, 1)
        if(u>c):
            if(u<c): t.insert(i, 1)  
            if(u>=c and u<=d): t.insert(i,1-2*(pow(((u-c)/(e-c)),2)))                  
            if(u>d and u<=e): t.insert(i,1-(1-2*(pow(((u-e)/(e-c)),2))))                 
            if(u>e): t.insert(i, 0) 

        

pi_ciz(a, b, c, d, e)          
plt.plot(x,t, color="black")


#----------------------

ku=[]
de=[]
gen=[]
yog=[]

def kuvvet(t):
    p= int(input("p değeri girin:"))
    for  i,ul in enumerate(t):
        ku.insert(i, pow(ul,p))

def derisme(t):
    for  i,ul in enumerate(t):
        de.insert(i, pow(ul,2))
       
def genisleme(t):
    for  i,ul in enumerate(t):
        gen.insert(i, pow(ul,0.5))
       
def yogunlasma(t):
    for  i,ul in enumerate(t):
        if (0<= ul <= 0.5):
            yog.insert(i, 2*(pow(ul,2)))
        if (0.5< ul <= 1):
            yog.insert(i, 1 - 2*(pow((1-ul),2)))
       

kuvvet(t)
derisme(t)
genisleme(t)
yogunlasma(t)

plt.plot(x, ku, color="blue",  linestyle='-.', label="kuvvet")
plt.plot(x,de, color="orange",  linestyle='--', label="derisme")
plt.plot(x,gen, color="red", linestyle='--', label="genisleme")
plt.plot(x,yog, color="green", linestyle=':', label="yogunlasma")

# Function add a hint
plt.legend();