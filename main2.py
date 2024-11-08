import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="film"
)
mycursor = mydb.cursor()

sql = "INSERT INTO film (Titolo, Regista, Genere, Anno_uscita, Cast_principale) VALUES (%s, %s, %s, %s, %s)"

film = [
    ("Il Padrino", "Francis Ford Coppola", "Gangster", 1972, "Marlon Brando, Al Pacino"),
    ("Schindler's List", "Steven Spielberg", "Drammatico", 1993, "Liam Neeson"),
    ("Il Signore degli Anelli: La Compagnia dell'Anello", "Peter Jackson", "Fantasy", 2001, "Elijah Wood, Ian McKellen"),
    ("Pulp Fiction", "Quentin Tarantino", "Noir", 1994, "John Travolta, Samuel L. Jackson"),
    ("Interstellar", "Christopher Nolan", "Sci-fi", 2014, "Matthew McConaughey, Anne Hathaway"),
    ("Forrest Gump", "Robert Zemeckis", "Drammatico", 1994, "Tom Hanks"),
    ("Inception", "Christopher Nolan", "Sci-fi", 2010, "Leonardo DiCaprio, Joseph Gordon-Levitt"),
    ("Il Gladiatore", "Ridley Scott", "Storico", 2000, "Russell Crowe"),
    ("The Shawshank Redemption", "Frank Darabont", "Drammatico", 1994, "Tim Robbins, Morgan Freeman")
]

mycursor.executemany(sql, film)
mydb.commit()
print(mycursor.rowcount, "record sono stati inseriti.")
