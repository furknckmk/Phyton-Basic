# -*- coding: utf-8 -*-

import sqlite3
# def selectOperasyonlari():
#   connection = sqlite3.connect("chinook.db")

# # cursor = connection.execute("""select * from customers 
                            
# #                             order by FirstName desc""")

# # for row in cursor:
# #     print("First Name = "+ row[1])
# #     print("Last Name = "+ row[2])
# #     print("city = "+ row[5])
# #     print("*********")
# cursor = connection.execute("""select FirstName,LastName 
#                             from customers where FirstName like '%ja' """)
# for row in cursor:
#     print("city = "+ row[0])
#     print("count = "+ str(row[1]))
   
#     print("*********")
# connection.close()

# selectOperasyonlari()

# def insertCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""insert into customers (firstName,lastName,city,email) 
#                        values('Furkan','Cakmak','Hatay','furkancakmak31@gmail.com')""")
#     connection.commit()
#     connection.close()       

# insertCustomer()                

# def updateCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""update customers set city ='Istanbul' where city='Hatay' """)
#     connection.commit()
#     connection.close()
    
# updateCustomer()

# def deleteCustomer():
#     connection = sqlite3.connect("chinook.db")
#     connection.execute("""Delete from customers where customerid=60 """)
#     connection.commit()
#     connection.close()
    
# deleteCustomer()

def joinOperations():
    
    connection = sqlite3.connect("chinook.db")
    cursor = connection.execute("""select albums.Title, artists.Name from artists inner join albums on artists.ArtistId=albums.ArtistId
                                order by artists.Name asc""")

    for row in cursor:
        print("Title = "+ row[0])
        print("Name = "+ row[1])

    connection.close()

joinOperations()

















