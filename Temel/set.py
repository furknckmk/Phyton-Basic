# -*- coding: utf-8 -*-

mySet = {"Furkan","Derin","Salih","Ahmet"}
print(mySet)

for student in mySet:
    print(student)
    
    
print("Derin" in mySet)

if "Derin" in mySet:
    print("Listede Var")
    
    
    mySet.add("Ali")
    print(mySet)
    
    
    mySet.update(["Merve",'Mert','Selin'])
    print(mySet)
    
    print(len(mySet))
    
    mySet.remove("Selin")
    print(len(mySet))
    
    mySet.discard("Selin")
    print(len(mySet))
    
    x=mySet.pop()
    print(len(mySet))
    del mySet
    print(mySet)