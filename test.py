import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root"
)

print(mydb)