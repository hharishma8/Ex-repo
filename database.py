import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="harishma_8",
  database="idea_customers"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE student (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")
