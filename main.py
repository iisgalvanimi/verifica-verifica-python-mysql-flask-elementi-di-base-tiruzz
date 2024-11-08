import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS film")

mydb.database = "film"

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS film (
        Id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        Titolo VARCHAR(255),
        Regista VARCHAR(255),
        Genere VARCHAR(255),
        Anno_uscita INT,
        Cast_principale VARCHAR(255)
    )
""")