# -*- coding: utf-8 -*-

sayi = int(input("Sayi Giriniz"))
asalMi = False
for x in range(2,sayi):
    if (sayi % x) == 0:
        print(asalMi)
        break
    else:
        asalMi=True
        print(asalMi)
        break
# if asalMi=="evet":
#     print("ASAL")
# else:
#     print("ASAL DEGIL")

    
        
    
        
