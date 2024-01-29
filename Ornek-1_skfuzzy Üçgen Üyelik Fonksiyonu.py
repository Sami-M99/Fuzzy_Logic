"""
Örnekler - Sayfa 26

Örnek-1:
İkinci el bir aracın fiyatını tahmin etmek için kullanılan bir bulanık sistem taslayalım. 
Sistem iki adet giriş parametresine sahip olsun. Bunlar araç modeli ve aracın kilometresi olsun. 
Çıkış parametresi aracın fiyatı olmaktadır. 
Giriş parametrelerinin aralık değerleri
	 • Model için [2002-2012] 
	 • Km için [0-100.000] 
Çıkış parametresinin aralık değerleri 
Fiyat İçin [0-40.000] 

Kural tabanındaki bulanık kurallar 
Kural I: Eğer model düşük ve kilometresi yüksek ise O halde araç fiyatı düşüktür. 
Kural 2: Eğer model orta ve kilometresi orta ise O halde araç fiyatı ortadır. 
Kural 3: Eğer model yüksek ve kilometresi düşük ise O halde araç fiyatı yüksektir. 
2011 model ve 25 bin kilometrede olan bir aracın fiyatının Mamdani çıkarım yöntemi kullanılarak tahmin edelim. 

"""
import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

var_model= np.arange(2002,2013,1)
var_km = np.arange(0,100001,100)
var_fiyat= np.arange(0,40001,10)

# Model 
set_model_dusuk = mf.trimf(var_model, [2002,2002,2007])
set_model_orta = mf.trimf(var_model, [2002,2007,2012])
set_model_yuksek = mf.trimf(var_model, [2007,2012,2012])

fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))
ax0.plot(var_model,set_model_dusuk,'green',linewidth=2, label='Düşük')
ax0.plot(var_model,set_model_orta,'red',linewidth=2, label='Orta')
ax0.plot(var_model,set_model_yuksek,'blue',linewidth=2, label='Yüksek')
ax0.set_xticks(np.arange(min(var_model),2013,1))
ax0.set_yticks(np.arange(0,1.1,0.1))
ax0.set_title("Model")
ax0.legend()

# KM
set_km_dusuk = mf.trimf(var_km, [0,0,50000])
set_km_orta= mf.trimf(var_km, [0,50000,100000])
set_km_yuksek = mf.trimf(var_km, [50000,100000,100000])

ax1.plot(var_km,set_km_dusuk,'green',linewidth=2, label='Düşük')
ax1.plot(var_km,set_km_orta,'red',linewidth=2, label='Orta')
ax1.plot(var_km,set_km_yuksek,'blue',linewidth=2, label='Yüksek')
ax1.set_title("KM")
ax1.legend()

# Fiyat
set_fiyat_dusuk = mf.trimf(var_fiyat, [0,0,20000])
set_fiyat_orta = mf.trimf(var_fiyat, [0,20000,40000])
set_fiyat_yuksek = mf.trimf(var_fiyat, [20000,40000,40000])

ax2.plot(var_fiyat,set_fiyat_dusuk,'green',linewidth=2, label='Düşük')
ax2.plot(var_fiyat,set_fiyat_orta,'red',linewidth=2, label='Orta')
ax2.plot(var_fiyat,set_fiyat_yuksek,'blue',linewidth=2, label='Yüksek')
ax2.set_title("Fiyat")
ax2.legend()

# input values
input_model = 2011
inpur_km = 25000

# Model icin
model_fit_dusuk = fuzz.interp_membership(var_model, set_model_dusuk, input_model)
model_fit_orta= fuzz.interp_membership(var_model, set_model_orta, input_model)
model_fit_yuksek = fuzz.interp_membership(var_model, set_model_yuksek, input_model)

ax0.plot([input_model,input_model],[0,model_fit_dusuk],'k',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_dusuk,model_fit_dusuk],'k',linewidth=1, linestyle='--')

ax0.plot([input_model,input_model],[0,model_fit_orta],'k',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_orta,model_fit_orta],'k',linewidth=1, linestyle='--')

ax0.plot([input_model,input_model],[0,model_fit_yuksek],'k',linewidth=1, linestyle='--')
ax0.plot([2002,input_model],[model_fit_yuksek,model_fit_yuksek],'k',linewidth=1, linestyle='--')

# KM icin
km_fit_dusuk = fuzz.interp_membership(var_km, set_km_dusuk, inpur_km)
km_fit_orta= fuzz.interp_membership(var_km, set_km_orta, inpur_km)
km_fit_yuksek = fuzz.interp_membership(var_km, set_km_yuksek, inpur_km)

ax1.plot([inpur_km,inpur_km],[0,km_fit_dusuk],'k',linewidth=1, linestyle='--')
ax1.plot([0,inpur_km],[km_fit_dusuk,km_fit_dusuk],'k',linewidth=1, linestyle='--')

ax1.plot([inpur_km,inpur_km],[0,km_fit_orta],'k',linewidth=1, linestyle='--')
ax1.plot([0,inpur_km],[km_fit_orta,km_fit_orta],'k',linewidth=1, linestyle='--')

ax1.plot([inpur_km,inpur_km],[0,km_fit_yuksek],'k',linewidth=1, linestyle='--')
ax1.plot([0,inpur_km],[km_fit_yuksek,km_fit_yuksek],'k',linewidth=1, linestyle='--')

# Kurallar
rule1 = np.fmin(np.fmin(model_fit_dusuk,km_fit_yuksek),set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta,km_fit_orta),set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek,km_fit_dusuk),set_fiyat_yuksek)

ax3.plot(var_fiyat,rule1,'red', linestyle='--', linewidth=2, label='Rule-1')
ax3.plot(var_fiyat,rule2, 'blue', linestyle='-.', linewidth=2, label='Rule-2')
ax3.plot(var_fiyat,rule3, 'green', linestyle=':', linewidth=2, label='Rule-3')
ax3.set_title("Kurallar")
ax3.legend()

o = np.fmax(rule1,rule2)
out_set = np.fmax(o,rule3)
ax4.plot(var_fiyat,out_set, 'blue', linestyle='-', linewidth=10, label='out')
ax4.set_title("Kurallar Birleşimi")

# ------------------------------------
centroid = fuzz.defuzz(var_fiyat, out_set, 'centroid')
print('Fiyat (centroid) ==> ',centroid)

bisector = fuzz.defuzz(var_fiyat, out_set, 'bisector')
print('Fiyat (bisector) ==> ',bisector)

mom = fuzz.defuzz(var_fiyat, out_set, 'mom')
print('Fiyat (mom) ==> ',mom)

lom = fuzz.defuzz(var_fiyat, out_set, 'lom')
print('Fiyat (lom) ==> ',lom)

som = fuzz.defuzz(var_fiyat, out_set, 'som')
print('Fiyat (som) ==> ',som)



# ---------------------------
def draw(item):
    result = fuzz.interp_membership(var_fiyat, out_set, item)
    ax4.plot([0,item],[result,result],'r')
    ax4.plot([item,item],[0,result],'r')
    
draw(centroid)
draw(bisector)
draw(mom)
draw(lom)
draw(som)