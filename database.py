import sqlite3

connection = sqlite3.connect("database.sqlite")
cursor = connection.cursor()

cursor.execute("""
    create table if not exists phrases(
        id integer primary key,
        phrase text,
        answer text
    )
""")
cursor.execute("insert into phrases values (0, 'privet','poka')")
cursor.execute("insert into phrases values (1, 'саня', 'не списывай')")
cursor.execute("insert into phrases values (2, 'gg', 'vp')")


connection.commit()
connection.close()