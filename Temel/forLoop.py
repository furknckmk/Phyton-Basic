# -*- coding: utf-8 -*-
sehirler = ["Ankara","Istanbul","Izmir"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])
#%% for intro
for sehir in sehirler:
    if sehir =="Istanbul":
        continue
    print(sehir + "Icin Kod = "+sehir[0:3])         
   
#%% for intro   
for x in range(1,10,2):
    print(x)