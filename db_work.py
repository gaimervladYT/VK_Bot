import sqlite3
connect = sqlite3.connect('cars.sqlite')
cursor = connect.cursor()
#"""


cursor.execute("insert into owners values (4,'Саня','126')")
cursor.execute("insert into owners values (5,'Виктор','127')")
cursor.execute("insert into owners values (6,'Андрей','128')")
cursor.execute("insert into owners values (7,'Андрей','129')")
cursor.execute("insert into owners values (8,'Ира','130')")



cursor.execute("insert into models values (4,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (5,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (6,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (7,'Lada','Zhaporogec','Russia')")
cursor.execute("insert into models values (8,'Lada','Zhaporogec','Russia')")



cursor.execute("insert into cars values (5,671,'gray', 2,4)")
cursor.execute("insert into cars values (6,672,'purple', 2,5)")
cursor.execute("insert into cars values (7,673,'green', 2,6)")
cursor.execute("insert into cars values (8,674,'yellow', 2,7)")


connect.commit()

connect.close()
#"""




