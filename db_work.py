import sqlite3
connect = sqlite3.connect('cars.sqlite')
cursor = connect.cursor()


#"""
cursor.execute("""
CREATE table owners (
id integer primary key,
owner text,
driver_card integer
""")

cursor.execute("""
CREATE table models (
id integer primary key,
mark text,
model text,
prod_country text
""")

cursor.execute("""
CREATE table cars (
id integer primary key,
number integer,
color text,
id_owner integer,
id_model integer,
FOREIGN KEY (id_owner) REFERENCES owners (id)
FOREIGN KEY (id_model) REFERENCES models (id)
""")

cursor.execute("insert into owners values (1,'Вася','123')")
cursor.execute("insert into owners values (2,'Ира','124')")
cursor.execute("insert into owners values (3,'Игорь','125')")
cursor.execute("insert into owners values (4,'Саня','126')")
cursor.execute("insert into owners values (5,'Виктор','127')")
cursor.execute("insert into owners values (6,'Андрей','128')")
cursor.execute("insert into owners values (7,'Андрей','129')")
cursor.execute("insert into owners values (8,'Ира','130')")

cursor.execute("insert into models values (1,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (2,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (3,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (4,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (5,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (6,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (7,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (8,'Lada','Zhaporogec','Russia')")

cursor.execute("insert into cars values (1,667,'gray', 2,0)")
cursor.execute("insert into cars values (2,668,'gray', 2,1)")
cursor.execute("insert into cars values (3,669,'gray', 2,2)")
cursor.execute("insert into cars values (4,670,'gray', 2,3)")
cursor.execute("insert into cars values (5,671,'gray', 2,4)")
cursor.execute("insert into cars values (6,672,'purple', 2,5)")
cursor.execute("insert into cars values (7,673,'green', 2,6)")
cursor.execute("insert into cars values (8,674,'yellow', 2,7)")

cursor.execute("""
  SELECT cars.number,cars.color,owners.owner,models.mark
  FROM cars,owners,models
  WHERE cars.id_owner=owners.id and cars.id_model=models.
""")
print(cursor.fetchall())
connect.commit()

connect.close()
#"""




