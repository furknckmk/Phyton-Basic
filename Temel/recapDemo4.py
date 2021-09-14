# -*- coding: utf-8 -*-

ogrenciler = ["Furkan","Salih","Derin","Ali"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()