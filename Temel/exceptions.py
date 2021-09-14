# -*- coding: utf-8 -*-

try:
    sayi=int(input("Sayi Giriniz :"))
except (ValueError,ZeroDivisionError):
    print("Tip Uyusmazligi : Lutfen Sayi giriniz")    
    
    
except:
    print("Bir Hata Olustu!")


print("Bitti")