import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "store" #"pythonprogramming"
)

# print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE pythonprogramming")

#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
  #  print(x)



#mycursor.execute("CREATE TABLE Customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#    print(x)

mycursor.execute("SELECT * FROM USERS")

#myresult = mycursor.fetchall()
myresult1 = mycursor.fetchone()

#for x in myresult:
 #   print(x)

print(myresult1)