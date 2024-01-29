""" 
Örnek-1_optimize - Sayfa 38 

Ödev:
Örnek-1.py’deki kodları optimize edin. 
Tekrarlayan işlemler için fonksiyon yazarak kodları kısaltın. 
"""


import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

var_model= np.arange(2002,2013,1)
var_km = np.arange(0,100001,100)
var_fiyat= np.arange(0,40001,10)

def plotCizme(ax,var,sets,title):
    for item in sets:
        ax.plot(var,sets[item],linewidth=2, label= item)
    ax.set_title(title)
    ax.legend()


# Model 
set_model_dusuk = mf.trimf(var_model, [2002,2002,2007])
set_model_orta = mf.trimf(var_model, [2002,2007,2012])
set_model_yuksek = mf.trimf(var_model, [2007,2012,2012])

fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))

plotCizme(ax0,var_model,{'Düşük':set_model_dusuk,'Orta':set_model_orta,'Yüksek':set_model_yuksek},"Model")

# ax0.plot(var_model,set_model_dusuk,'green',linewidth=2, label='Düşük')
# ax0.plot(var_model,set_model_orta,'red',linewidth=2, label='Orta')
# ax0.plot(var_model,set_model_yuksek,'blue',linewidth=2, label='Yüksek')
# ax0.set_xticks(np.arange(min(var_model),2013,1))
# ax0.set_yticks(np.arange(0,1.1,0.1))
# ax0.set_title("Model")
# ax0.legend()

# KM
set_km_dusuk = mf.trimf(var_km, [0,0,50000])
set_km_orta= mf.trimf(var_km, [0,50000,100000])
set_km_yuksek = mf.trimf(var_km, [50000,100000,100000])

plotCizme(ax1,var_km,{'Düşük':set_km_dusuk,'Orta':set_km_orta,'Yüksek':set_km_yuksek},'KM')

# ax1.plot(var_km,set_km_dusuk,'green',linewidth=2, label='Düşük')
# ax1.plot(var_km,set_km_orta,'red',linewidth=2, label='Orta')
# ax1.plot(var_km,set_km_yuksek,'blue',linewidth=2, label='Yüksek')
# ax1.set_title("KM")
# ax1.legend()


# Fiyat
set_fiyat_dusuk = mf.trimf(var_fiyat, [0,0,20000])
set_fiyat_orta = mf.trimf(var_fiyat, [0,20000,40000])
set_fiyat_yuksek = mf.trimf(var_fiyat, [20000,40000,40000])

plotCizme(ax2,var_fiyat,{'Düşük':set_fiyat_dusuk,'Orta':set_fiyat_orta,'Yüksek':set_fiyat_yuksek},'Fiyat')

# ax2.plot(var_fiyat,set_fiyat_dusuk,'green',linewidth=2, label='Düşük')
# ax2.plot(var_fiyat,set_fiyat_orta,'red',linewidth=2, label='Orta')
# ax2.plot(var_fiyat,set_fiyat_yuksek,'blue',linewidth=2, label='Yüksek')
# ax2.set_title("Fiyat")
# ax2.legend()

# input values
input_model = 2011
inpur_km = 25000

# Model icin
model_fit_dusuk = fuzz.interp_membership(var_model, set_model_dusuk, input_model)
model_fit_orta= fuzz.interp_membership(var_model, set_model_orta, input_model)
model_fit_yuksek = fuzz.interp_membership(var_model, set_model_yuksek, input_model)

def uyelik(ax,xStart,inputValue,fit):
    ax.plot([inputValue,inputValue],[0,fit],'red',linewidth=1, linestyle='--')
    ax.plot([xStart,inputValue],[fit,fit],'red',linewidth=1, linestyle='--')
    

uyelik(ax0,var_model[0],input_model,model_fit_dusuk)
uyelik(ax0,var_model[0],input_model,model_fit_orta)
uyelik(ax0,var_model[0],input_model,model_fit_yuksek)

# ax0.plot([input_model,input_model],[0,model_fit_dusuk],'k',linewidth=1, linestyle='--')
# ax0.plot([2002,input_model],[model_fit_dusuk,model_fit_dusuk],'k',linewidth=1, linestyle='--')

# ax0.plot([input_model,input_model],[0,model_fit_orta],'k',linewidth=1, linestyle='--')
# ax0.plot([2002,input_model],[model_fit_orta,model_fit_orta],'k',linewidth=1, linestyle='--')

# ax0.plot([input_model,input_model],[0,model_fit_yuksek],'k',linewidth=1, linestyle='--')
# ax0.plot([2002,input_model],[model_fit_yuksek,model_fit_yuksek],'k',linewidth=1, linestyle='--')

# KM icin
km_fit_dusuk = fuzz.interp_membership(var_km, set_km_dusuk, inpur_km)
km_fit_orta= fuzz.interp_membership(var_km, set_km_orta, inpur_km)
km_fit_yuksek = fuzz.interp_membership(var_km, set_km_yuksek, inpur_km)

uyelik(ax1,var_km[0],inpur_km,km_fit_dusuk)
uyelik(ax1,var_km[0],inpur_km,km_fit_orta)
uyelik(ax1,var_km[0],inpur_km,km_fit_yuksek)

# ax1.plot([inpur_km,inpur_km],[0,km_fit_dusuk],'k',linewidth=1, linestyle='--')
# ax1.plot([0,inpur_km],[km_fit_dusuk,km_fit_dusuk],'k',linewidth=1, linestyle='--')

# ax1.plot([inpur_km,inpur_km],[0,km_fit_orta],'k',linewidth=1, linestyle='--')
# ax1.plot([0,inpur_km],[km_fit_orta,km_fit_orta],'k',linewidth=1, linestyle='--')

# ax1.plot([inpur_km,inpur_km],[0,km_fit_yuksek],'k',linewidth=1, linestyle='--')
# ax1.plot([0,inpur_km],[km_fit_yuksek,km_fit_yuksek],'k',linewidth=1, linestyle='--')

# Kurallar
rule1 = np.fmin(np.fmin(model_fit_dusuk,km_fit_yuksek),set_fiyat_dusuk)
rule2 = np.fmin(np.fmin(model_fit_orta,km_fit_orta),set_fiyat_orta)
rule3 = np.fmin(np.fmin(model_fit_yuksek,km_fit_dusuk),set_fiyat_yuksek)

ax3.plot(var_fiyat,rule1,'red', linestyle='--', linewidth=2, label='Rule-1')
ax3.plot(var_fiyat,rule2, 'blue', linestyle='-.', linewidth=2, label='Rule-2')
ax3.plot(var_fiyat,rule3, 'green', linestyle=':', linewidth=2, label='Rule-3')
ax3.set_title("Kurallar")
ax3.legend()


def calculate(rules):
    maxVaules = rules[0]
    for rule in rules:
        maxVaules = np.fmax(maxVaules, rule)
    return maxVaules

out_set = calculate([rule1, rule2, rule3])
ax4.plot(var_fiyat,out_set, 'blue', linestyle='-', linewidth=10, label='out')
ax4.set_title("Kurallar Birleşimi")

# ------------------------------------

def draw(ax, x, mfx, item):
    result = fuzz.interp_membership(x, mfx, item)
    ax.plot([0,item],[result,result],'r')
    ax.plot([item,item],[0,result],'r')


def defuzz_draw(x, mfx, modes):
    for mode in modes:
        result = fuzz.defuzz(x, mfx, mode)
        print(f'Fiyat ({mode}) ==> {result}')
        draw(ax4, x, mfx, result)
        

defuzz_modes = ['centroid', 'bisector', 'mom', 'lom', 'som']
defuzz_draw(var_fiyat, out_set, defuzz_modes)

# centroid = fuzz.defuzz(var_fiyat, out_set, 'centroid')
# print('Fiyat (centroid) ==> ',centroid)

# bisector = fuzz.defuzz(var_fiyat, out_set, 'bisector')
# print('Fiyat (bisector) ==> ',bisector)

# mom = fuzz.defuzz(var_fiyat, out_set, 'mom')
# print('Fiyat (mom) ==> ',mom)

# lom = fuzz.defuzz(var_fiyat, out_set, 'lom')
# print('Fiyat (lom) ==> ',lom)

# som = fuzz.defuzz(var_fiyat, out_set, 'som')
# print('Fiyat (som) ==> ',som)



# ---------------------------

    
