import mysql.connector

mydb = mysql.connector.connect(
    host = "akmalsecond.mysql.pythonanywhere-services.com",
    user = "akmalsecond",
    password = "rootpassword",
    database = "users"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)