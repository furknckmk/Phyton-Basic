# -*- coding: utf-8 -*-

sayi1=int(input("1.Sayi Giriniz"))
sayi2=int(input("2.Sayi Giriniz"))
sayi3=int(input("3.Sayi Giriniz"))

if sayi1 > sayi2 and sayi1 > sayi3:
    print("En buyuk sayi :"+ str(sayi1))
elif sayi2 > sayi1 and sayi2>sayi3:
    print("En Buyuk Sayi :"+ str(sayi2))
else:
    print("En Buyuk Sayi :"+ str(sayi3))
