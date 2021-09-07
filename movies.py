import sqlite3

connection = sqlite3.connect('Movies.db')

cursor = connection.cursor()


command1 = Movies(movies_id INTEGER PRIMARY KEY, Movie_name TEXT, Actors TEXT, Actress TEXT, Director_name TEXT)---

cursor.execute(command1)

#add to Movies

execute("INSERT INTO Movies VALUES (1, 'Harrypotter', 'Daniel Radicliff', 'Emma Watson', 'David')")
execute("INSERT INTO Movies VALUES (2, 'Bahubali', 'Prabhas', 'Anushka', 'Rajamouli')")
execute("INSERT INTO Movies VALUES (3, 'Jersey', 'Nani', 'Shraddha', 'Gowtam')")

cursor("SELECT * FROM Movies")

results =  cursor.fetchall()

Print(results)
