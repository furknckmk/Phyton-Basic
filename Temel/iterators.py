# -*- coding: utf-8 -*-

sehirler = ["Ankara","Istanbul","Izmir","Van"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler:
    print(sehir)