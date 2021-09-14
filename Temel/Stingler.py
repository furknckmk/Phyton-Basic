# substring

mesaj = 'Merhaba Dunya'
print(mesaj[0:5])
yeniMesaj = mesaj[:5]
print(yeniMesaj)
#len
yeniMesaj2=mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

#Lower upper 
print(mesaj.upper())
print(mesaj.lower())


#replace
mesaj = mesaj.replace('u','e')
print(mesaj)

print(mesaj.replace('a','e'))

#Split ve strip

bilgi = 'Furkan;Cakmak;23;Hatay'.strip()
print(bilgi.split())
print(bilgi.split(';'))
print('Adi = '+bilgi.split(';')[0])

#input

#ad=input('Adiniz ? :')

sayi1 = input("Sayi 1 =")
sayi2 = input("Sayi 2 =")
print(int(sayi1)+ int(sayi2))


