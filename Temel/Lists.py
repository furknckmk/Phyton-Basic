# -*- coding: utf-8 -*-


# ogrenci1 = 'Engin'
# ogrenci2 = 'Furkan'
# ogrenci3 = 'Salih'

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)

ogrenciler = ['Engin','Furkan','Salih']
ogrenciler.append('Ahmet')
ogrenciler[0]='Veli'
print(ogrenciler[3])


ogrenciler.remove('Salih')
print(ogrenciler)
#List constructor
sehirler = list(('Ankara','Istanbul','Ankara'))
print(sehirler)
print(len(sehirler))

#diger fonksiyonlar

# print(sehirler.clear())
print("Ankara Sayisi ="+str(sehirler.count('Ankara')))#
print("Ankara index ="+str(sehirler.index('Ankara')))
sehirler.pop(1)
sehirler.insert(0,'Istanbul')
sehirler.reverse()
print(sehirler)
sehirler3=sehirler.copy()
sehirler2=sehirler

sehirler2[0]='izmir'
print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()
sehirler.reverse()
print(sehirler)
