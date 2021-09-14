# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 22 15:01:16 2021

# @author: MMFH V.3
# """
# import matematikModule as mm


# print("1 : Topla")
# print("2 : Cikar")
# print("3 : Bol")
# print("4 : Carp")

# x = int(input("Hangi Islemi Yapacaksin ? :"))

# if x == 1:
#     sayi1 = int(input("Toplanacak 1. Sayi :"))
#     sayi2 = int(input("Toplanacak 2. Sayi :"))
#     sonuc =  mm.topla(sayi1, sayi2)
#     print(sonuc)
    
# if x == 2:
#     sayi1 = int(input("Carpilacak 1. Sayi :"))
#     sayi2 = int(input("Carpilacak 2. Sayi :"))
#     sonuc =  mm.carp(sayi1, sayi2)
#     print(sonuc)

# if x == 3:
#     sayi1 = int(input("Bolunecek 1. Sayi :"))
#     sayi2 = int(input("Bolunecek 2. Sayi :"))
#     sonuc =  mm.bol(sayi1, sayi2)
#     print(sonuc)

# if x == 4:
#     sayi1 = int(input("Cikarilacak 1. Sayi :"))
#     sayi2 = int(input("Cikarilacak 2. Sayi :"))
#     sonuc =  mm.cikar(sayi1, sayi2)
#     print(sonuc)
    
# else:
#     print("Gecersiz Sayi Girisi!!")
 
    
 
def topla(sayi1,sayi2):
    return sayi1 + sayi2

def cikar(sayi1,sayi2):
    return sayi1 - sayi2

def carp(sayi1,sayi2):
    return sayi1 * sayi2

def bol(sayi1,sayi2):
    return sayi1 / sayi2
 
    
print("1 : Topla")
print("2 : Cikar")
print("3 : Carp")
print("4 : Bol")

secenek = int(input("Hangi Operasyon ? :"))

if secenek >4 or secenek < 1:
    print("Yanlis Secim Yaptiniz")

elif (secenek < 5) or (secenek > 0):
    sayi1 = int(input("1. Sayi? :"))
    sayi2 = int(input("2. Sayi? :"))
if secenek == "1":
    print(int(topla(sayi1, sayi2)))
elif secenek == "2":
        print(cikar(sayi1, sayi2)) 
elif secenek == "3":
     print(carp(sayi1, sayi2))

elif secenek == "4":
     print(bol(sayi1, sayi2))     
 
   
    
   
       








      
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    