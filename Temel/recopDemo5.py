# -*- coding: utf-8 -*-
import sys

liste = [7,'furkan',0,3,"6"]

for x in liste:
    try:
        
        print("Sayi: "+ str(x))
        sonuc = 1/int(x)
        
        print("Sonuc :" + str(sonuc))
        
    except ValueError:
        print(str(x)+"Bir Sayi Degil!")
        
    except ZeroDivisionError:
        print(str(x)+"")
        
    except:
         print(str(x)+"Hesaplanamadi")
         print("Sistem Diyor ki :"+ str(sys.exc_info()[0]))
         
    finally:
        print("Islemler Bitti")