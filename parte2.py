from flask import Flask, jsonify, request
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="film"
)

mycursor = mydb.cursor()
app = Flask(__name__)

def getAllData():
    mycursor.execute("SELECT * FROM film")
    rows = mycursor.fetchall()
    result = []
    for x in rows:
        result.append(x)
    return result



@app.route("/")
def index():
    data = getAllData()
    return jsonify({'film': data})

