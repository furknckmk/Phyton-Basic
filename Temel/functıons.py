# sehir = "Ankara"

# print(sehir.upper())
# print(sehir.endswith("a"))

def selamVer(isim = "Ziyaretci", soyIsim = " arkadas"):
    print("Merhaba " + isim + soyIsim) 
    
    
selamVer()
selamVer("Furkan")

# def dikUcgenAlaniHesapla(a,b):
#     return a*b/2



# alan = dikUcgenAlaniHesapla(int(input("1. Degeri Giriniz :")), int(input("2. Degeri Giriniz :")))

# print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(int(input("1. Degeri Giriniz :")), int(input("2. Degeri Giriniz :"))))