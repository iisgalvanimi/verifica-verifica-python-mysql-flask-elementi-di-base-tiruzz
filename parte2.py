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

def addfilm(data):
    query = "INSERT INTO film (Titolo, Regista, Genere, Anno_uscita, Cast_principale) VALUES (%s, %s, %s, %s, %s)"
    values = (data['Titolo'], data['Regista'], data['Genere'], data['Anno_uscita'], data["Cast_principale"])
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

def deletefilm(Id):
    mycursor = mydb.cursor()
    query = "DELETE FROM film WHERE Id = %s"
    mycursor.execute(query, (Id,))
    mydb.commit()
    rowcount = mycursor.rowcount
    mycursor.close()
    return rowcount

def updatefilm(Id, data):
    query = "UPDATE film SET Titolo = %s, Regista = %s, Genere = %s, Anno_uscita = %s, Cast_principale = %s WHERE id = %s"
    values = (data['Titolo'], data['Regista'], data['Genere'], data['Anno_uscita'], data["Cast_principale"], id)
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

@app.route("/dati")
def index():
    data = getAllData()
    return jsonify({'film': data})

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    if not data:
        return jsonify({'message': 'Nessun dato fornito'}), 400

    required_fields = ['Titolo', 'Regista', 'Genere', 'Anno_uscita', 'Cast_principale'] 
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti o errati'}), 400

    rows_inserted = addfilm(data)
    if rows_inserted == 1:
        return jsonify({'message': 'Film inserito con successo'}), 201 
    else:
        return jsonify({'message': 'Errore durante l inserimento'}), 500

@app.route("/delete/<int:Id>", methods=["DELETE"])
def delete(Id):
    rows_deleted = deletefilm(Id)
    if rows_deleted == 1:
        return jsonify({'message': 'Film eliminato'}), 200
    else:
        return jsonify({'message': 'ID non trovato'}), 404

@app.route("/update/<Id>", methods=["PUT"])
def update(Id):
    print(request.json)
    print("ciao")
    data = request.json
    
    required_fields = ['Titolo', 'Regista', 'Genere', 'Anno_uscita', 'Cast_principale']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti'}), 400

    rows_updated = updatefilm(Id, data)
    if rows_updated == 1:
        return jsonify({'message': 'Mammifero aggiornato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l aggiornamento o ID non trovato'}), 404



if __name__ == "__main__":
    app.run()

