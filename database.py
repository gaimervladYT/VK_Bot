import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

#cursor.execute("""
#    create table if not exists phrases(
#        id integer primary key,
#       phrase text,
#        answer text
#    )
#""")
#cursor.execute("insert into phrases values (0, 'Привет','Привет, как дела?')")
#cursor.execute("insert into phrases values (1, 'а у тибя как?', 'Отлично')")
#cursor.execute("insert into phrases values (2, 'Как Играть?', 'https://www.youtube.com/watch?v=YlkzLWgpClc')")
#cursor.execute("insert into phrases values (3, 'Пока', 'пока')")
cursor.execute("DELETE FROM phrases WHERE id = 7")
connection.commit()
connection.close()