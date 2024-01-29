"""
Ornekler - sayfa 3 

Ornek-4: 
Havaland徘ma Sistemi 
"""

import skfuzzy as fuzz
import skfuzzy.membership as mf
import numpy as np
import matplotlib.pyplot as plt

#%%
#-----------------------------De��i��kenler olu��turuluyor--------------
var_sicaklik=np.arange(20,81,1)
var_sicaklik_degisim=np.arange(0,5.1,0.1)
var_motorhizi=np.arange(100,1001,1)
#------------------------------------------------------------------

#%%
#----------------------S覺cakl覺k i癟in ��yelik Fonksiyonlar覺 Tan覺mlan覺yor
set_sicaklik_low=mf.trapmf(var_sicaklik,[20,25,30,40] )
set_sicaklik_medium=mf.trapmf(var_sicaklik, [30,50,55,80])
#----S覺cakl覺k i癟in Bulan覺k K羹meler ��izdiriliyor
fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(nrows=5,figsize=(15,20))
ax0.plot(var_sicaklik,set_sicaklik_low,'r',linewidth=2, label='Low')
ax0.plot(var_sicaklik,set_sicaklik_medium,'g',linewidth=2, label='Medium')
ax0.set_xticks(np.arange(min(var_sicaklik),81,1))
ax0.set_yticks(np.arange(0,1.1,0.1))
ax0.set_title("S覺cakl覺k")
ax0.legend()
#%%
#----S覺cakl覺k De��i��imi i癟in ��yelik Fonksiyonlar覺 Tan覺mlan覺yor
set_sd_low=mf.trapmf(var_sicaklik_degisim, [0,0.3,1,2])
set_sd_medium=mf.trapmf(var_sicaklik_degisim, [0.5,1.5,2.5,3.5])
set_sd_high=mf.trapmf(var_sicaklik_degisim, [1,3,4,5])

#----S覺cakl覺k De��i��imi i癟in Bulan覺k K羹meler ��izdiriliyor
ax1.plot(var_sicaklik_degisim,set_sd_low,'r',linewidth=2, label='Low')
ax1.plot(var_sicaklik_degisim,set_sd_medium,'g',linewidth=2, label='Med')
ax1.plot(var_sicaklik_degisim,set_sd_high,'b',linewidth=2, label='Heigh')
ax1.set_xticks(np.arange(min(var_sicaklik_degisim),5.1,0.2))
ax1.set_yticks(np.arange(0,1.1,0.1))
ax1.set_title("S覺cakl覺k De��i��imi")
ax1.legend()
#%%
#----Motor H覺z覺 i癟in ��yelik Fonksiyonlar覺 Tan覺mlan覺yor
set_motorhizi_slow=mf.trapmf(var_motorhizi, [100,200,400,500])
set_motorhizi_med=mf.trapmf(var_motorhizi, [300,450,600,700])
set_motorhizi_fast=mf.trapmf(var_motorhizi, [500, 650,800, 1000])
#----Motor H覺z覺 i癟in Bulan覺k K羹meler ��izdiriliyor
ax2.plot(var_motorhizi,set_motorhizi_slow,'r',linewidth=2, label='Slow')
ax2.plot(var_motorhizi,set_motorhizi_med,'g',linewidth=2, label='Medium')
ax2.plot(var_motorhizi,set_motorhizi_fast,'b',linewidth=2, label='Fast')
ax2.set_xticks(np.arange(min(var_motorhizi),1001,50))
ax2.set_yticks(np.arange(0,1.1,0.1))
ax2.set_title("Motor H覺z覺")
ax2.legend()
#%%
#-------------Hesaplama Yap覺lacak Giri�� de��erleri belirleniyor
input_sicaklik=35
input_sd=1
#%% Herbir Giri��in giri�� bulan覺k k羹melerine 羹yelik dereceleri hesaplan覺yor
sicaklik_fit_low=fuzz.interp_membership(var_sicaklik,set_sicaklik_low,input_sicaklik)
sicaklik_fit_med=fuzz.interp_membership(var_sicaklik,set_sicaklik_medium,input_sicaklik)

#��yelik dereceleri grafik 羹zerinde g繹steriliyor
#         [x1,x2],[y1,y2] ��eklinde d羹z 癟izgi verileri verilmelidir.
ax0.plot([input_sicaklik,input_sicaklik],[0,sicaklik_fit_low],'r',linewidth=1, linestyle='--')
ax0.plot([var_sicaklik[0],input_sicaklik],[sicaklik_fit_low,sicaklik_fit_low],'r',linewidth=1, linestyle='--')
ax0.plot([input_sicaklik,input_sicaklik],[0,sicaklik_fit_med],'r',linewidth=1, linestyle='--')
ax0.plot([var_sicaklik[0],input_sicaklik],[sicaklik_fit_med,sicaklik_fit_med],'r',linewidth=1, linestyle='--')


sd_fit_low=fuzz.interp_membership(var_sicaklik_degisim,set_sd_low,input_sd)
sd_fit_med=fuzz.interp_membership(var_sicaklik_degisim,set_sd_medium,input_sd)
sd_fit_high=fuzz.interp_membership(var_sicaklik_degisim,set_sd_high,input_sd)
#��yelik dereceleri grafik 羹zerinde g繹steriliyor
#         [x1,x2],[y1,y2] ��eklinde d羹z 癟izgi verileri verilmelidir.
ax1.plot([input_sd,input_sd],[0,sd_fit_low],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_sd],[sd_fit_low,sd_fit_low],'r',linewidth=1, linestyle='--')
ax1.plot([input_sd,input_sd],[0,sd_fit_med],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_sd],[sd_fit_med,sd_fit_med],'r',linewidth=1, linestyle='--')
ax1.plot([input_sd,input_sd],[0,sd_fit_high],'r',linewidth=1, linestyle='--')
ax1.plot([0,input_sd],[sd_fit_high,sd_fit_high],'r',linewidth=1, linestyle='--')
#%%
#Kurallar olu��turuluyor ve uygulan覺yor Mamdani  #min metodu uygulan覺yor
rule1 = np.fmin(np.fmin(sicaklik_fit_low, sd_fit_low), set_motorhizi_fast)
rule2 = np.fmin(np.fmin(sicaklik_fit_med, sd_fit_med), set_motorhizi_slow)
rule3 = np.fmin(np.fmin(sicaklik_fit_low, sd_fit_med), set_motorhizi_fast)
rule4 = np.fmin(np.fmin(sicaklik_fit_med, sd_fit_low), set_motorhizi_med)
#max-癟arp覺m i癟in a��a��覺daki kurallar kullan覺labilir.
# rule1 = (np.fmin(model_fit_dusuk, km_fit_yuksek)* set_fiyat_dusuk)
# rule2 = (np.fmin(model_fit_orta, km_fit_orta)* set_fiyat_orta)
# rule3 = (np.fmin(model_fit_yuksek, km_fit_dusuk)* set_fiyat_yuksek)
 
ax3.plot(var_motorhizi,rule1,'r', linestyle='--', linewidth=1, label='Rule-1')
ax3.plot(var_motorhizi,rule2, 'b', linestyle='-.', linewidth=2, label='Rule-2')
ax3.plot(var_motorhizi,rule3, 'g', linestyle=':', linewidth=2, label='Rule-3')
ax3.plot(var_motorhizi,rule4, 'y', linestyle=':', linewidth=2, label='Rule-4')
ax3.set_xticks(np.arange(min(var_motorhizi),1001,50))
ax3.set_yticks(np.arange(0,1.1,0.1))
ax3.set_title("Her bir kuraldan elde edilen 癟覺k覺�� k羹meleri")
ax3.legend()
#---------------------------------------------------------------------------------------------

#Her bir kuraldan elde edilen ��覺k覺��lar覺n Maksimumu Al覺narak birle��tirme (aggretitaion) yap覺l覺yor
out1=np.fmax(rule1,rule2)
out2=np.fmax(out1,rule3) 
out_set_final=np.fmax(out2,rule4) #Nihai bulan覺k 癟覺k覺�� k羹memiz
ax4.plot(var_motorhizi,out_set_final, 'b', linestyle='-', linewidth=10, label='out')
#ax4.fill_between(var_motorhizi,out_set_final, 'b', linestyle=':', linewidth=2, label='out')
ax4.set_xticks(np.arange(min(var_motorhizi),1001,50))
ax4.set_yticks(np.arange(0,1.1,0.1))
ax4.set_title("��覺k覺��-Bulan覺k K羹me Birle��imi")



#%%
#Durulama 襤��lemi Yap覺l覺yor
#Durulama Y繹ntemleri
# 'centroid' ��� Centroid of the area under the output fuzzy set
# 'bisector' ��� Bisector of the area under the output fuzzy set
# 'mom' ��� Mean of the values for which the output fuzzy set is maximum
# 'lom' ��� Largest value for which the output fuzzy set is maximum
# 'som' ��� Smallest value for which the output fuzzy set is maximum

defuzzified_centroid = fuzz.defuzz(var_motorhizi, out_set_final, 'centroid') 
print("H覺z(centroid)=",defuzzified_centroid)

defuzzified_bisector = fuzz.defuzz(var_motorhizi, out_set_final, 'bisector') 
print("H覺z(bisector)=",defuzzified_bisector)

defuzzified_mom = fuzz.defuzz(var_motorhizi, out_set_final, 'mom') 
print("H覺z(mom)=",defuzzified_mom)

defuzzified_lom = fuzz.defuzz(var_motorhizi, out_set_final, 'lom') 
print("H覺z(lom)=",defuzzified_lom)

defuzzified_som = fuzz.defuzz(var_motorhizi, out_set_final, 'som') 
print("H覺z(som)=",defuzzified_som)

for i in range(5):
    if (i==0):hangisi=defuzzified_centroid
    elif(i==1):hangisi=defuzzified_bisector
    elif(i==2):hangisi=defuzzified_mom
    elif(i==3):hangisi=defuzzified_lom
    else:hangisi=defuzzified_som
    
    #hangisi=defuzzified_centroid
    result = fuzz.interp_membership(var_motorhizi, out_set_final, hangisi)
    ax4.plot([0,hangisi],[result,result],'r')
    ax4.plot([hangisi,hangisi],[0,result],'r')
#%%
#----��覺k覺��覺n her bir 癟覺k覺�� 羹yelik fonksiyonuna 羹yeli��i hesaplan覺yor
print("\n��覺k覺��覺n Slow K羹mesine ��yeli��i=",fuzz.interp_membership(var_motorhizi,set_motorhizi_slow,hangisi))
print("��覺k覺��覺n Medium K羹mesine ��yeli��i=",fuzz.interp_membership(var_motorhizi,set_motorhizi_med,hangisi))
print("��覺k覺��覺n Fast K羹mesine ��yeli��i=",fuzz.interp_membership(var_motorhizi,set_motorhizi_fast,hangisi))


