# -*- coding: utf-8 -*-

f = open("musteriler.txt")
# print(f.read())
print("***********")


# print(f.readline())

for l in f:
    print(l)
    
f.close()
#r Read, a append, w write, x create

# fileToAppend = open("ogrenciler2.txt","a")
# fileToAppend.write("\n")
# fileToAppend.write("Ahmet")
# fileToAppend.close()

import os
if os.path.exists("ogrenciler2.txt"):    
    os.remove("ogrenciler2.txt")
    
else:
    print("Dosya Yok")