# -*- coding: utf-8 -*-

def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    return a/b

def kontrol():
    deger = None
    secim =print(input("Programa Devam Etmek Istiyor musunuz ? E == 'E ye Basiniz.'")) 
    if secim=='e' or secim== 'E':
        deger = False
    else:
        deger = True        

while True:
    try:
        secim = int(input("1-Topla \n2-Cikar\n3-Carp\n4-Bol\nSecim Yapiniz :"))
        
        if secim == 1:
            sayi1=float(input("Birinci Sayiyi Giriniz :"))
            sayi2=float(input("Ikinci Sayiyi Giriniz :"))
            print("Sonuc :" + str(topla(sayi1,sayi2)))
        
        elif secim == 2:
            sayi1=float(input("Birinci Sayiyi Giriniz :"))
            sayi2=float(input("Ikinci Sayiyi Giriniz :"))
            print("Sonuc :" + str(cikar(sayi1,sayi2)))
            
        elif secim == 3:
            sayi1=float(input("Birinci Sayiyi Giriniz :"))
            sayi2=float(input("Ikinci Sayiyi Giriniz :"))
            print("Sonuc :" + str(carp(sayi1,sayi2)))
        elif secim == 4:
            sayi1=float(input("Birinci Sayiyi Giriniz :"))
            sayi2=float(input("Ikinci Sayiyi Giriniz :"))
            print("Sonuc :" + str(bol(sayi1,sayi2)))
        
        kontrol= kontrol()
        if kontrol:
            break
        
    except ValueError:
        print("Verdiginiz Deger Hatali Program Yeniden Calistiriliyor")

