
"""
Hafta2 - Sayfa 29
Ödev-1: Aşağıdaki sürekli zamanlı bulanık küme üyelik 
fonksiyonunu Python programlama dilinde çizdiriniz? 
Verilen bir X değerinin üyelik derecesini hesaplatıp ekrana yazdırın?
"""


import matplotlib.pyplot as plt
import numpy as np

# # Sürekli zamanlı bulanık küme üyelik fonksiyonu
# def fuzzy_membership(x):
#     return 1 / (1 + 10 * (x - 5)**2)

# # X değerleri
# x_values = np.linspace(0, 10, 1000)

# # Fonksiyon değerleri
# y_values = fuzzy_membership(x_values)

# # Grafiği çizdirme
# plt.plot(x_values, y_values, label='Fuzzy Membership Function')
# plt.title('Sürekli Zamanlı Bulanık Küme Üyelik Fonksiyonu')
# plt.xlabel('X Değeri')
# plt.ylabel('Üyelik Derecesi')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Belirli bir X değeri için üyelik derecesini hesaplatma ve yazdırma
# specific_x = 7  # İstediğiniz X değerini burada belirtin
# membership_degree = fuzzy_membership(specific_x)
# print(f'X = {specific_x} için Üyelik Derecesi: {membership_degree}')


"""----------- Another Solution --------"""

x=np.arange(1,10,0.1)
z=[]

for i, tutx in enumerate(x):
    z.insert(i,(1/(1+(10*(pow(tutx-5,2))))))



userx=float(input("1-10 arasında değer girin:"))
mx=(1/(1+(10*(pow(userx-5,2)))))
print("üyelik derecesi: ",mx)

x1,y1=[userx,userx],[0,mx]
x2,y2=[0,userx],[mx,mx]

plt.plot(x,z, color="black")
plt.plot(x1,y1,marker="o",color="green")
plt.plot(x2,y2, marker="o",color="red")
