# -*- coding: utf-8 -*-

class Matematik:
    
    def __init__(self,say1,say2):
        self.say1= say1
        self.say2= say2
    
 
    def topla(self):
        return self.say1+self.say2
    
    def cikar(self):    
        return self.say1-self.say2
    
    def carp(self):    
        return self.say1*self.say2
    
    def bol(self):    
        return self.say1/self.say2
    

matematik = Matematik(2,78)

print("Toplam = "+ str(matematik.topla()))

# #%%

# class Person:
#     def __init__(self,firstName,lastName,age):
#         self.firstName = firstName
#         self.lastName=lastName
#         self.age = age
        
        
# person1=("Furkan", "Cakmak", 23)
# print(person1)

# class Worker(Person):
#     def __init__(self,salary):
#         self.salary=salary

# class Customer(Person):
#     def __init__(self,creditCardNumber):
#         self.creditCardNumber=creditCardNumber
        

# ahmet = Worker()
# mehmet = Customer()
