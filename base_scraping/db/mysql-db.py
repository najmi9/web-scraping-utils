import mysql.connector

class DataBase():
	def __init__(self, DATABASE_NAME, host, user, password):
		try:
			db = mysql.connector.connect(
				host=host,
				user=user,
				password=password
			)
			mycursor = db.cursor()
			mycursor.execute("SHOW DATABASES")
			is_db_exist = False

			for dbase in mycursor:
				if (DATABASE_NAME, ) == dbase:
					is_db_exist = True

			if not is_db_exist:
				mycursor.execute("CREATE DATABASE {}".format(DATABASE_NAME))
				print('data base created  !')

			self.db = mysql.connector.connect(
				host=host,
				user=user,
				password=password,
				database=DATABASE_NAME
			)
		except Exception as e:
			print(e)
	# columns = ['age INT', 'name VARCHAR(255)', 'desc TEXT']
	def create_tabe(self, table_name, columns):
		columns.insert(0, "id INT AUTO_INCREMENT PRIMARY KEY")
		cursor = self.db.cursor()
		try:
			sql = "DROP TABLE IF EXISTS {}".format(table_name)
			cursor.execute(sql)
			sql = "CREATE TABLE {}{}".format(table_name, tuple(columns)).replace("'", '')
			cursor.execute(sql)
		except Exception as e:
			print(e)

	def drop_table(self, table):
		cursor = self.db.cursor()
		try:
			sql = "DROP TABLE IF EXISTS {}".format(table)
			cursor.execute(sql)
		except Exception as e:
			print(e)

	# data={"name"="name_value", "age"="age_value"}
	def insert_into_table(self, table_name, **data):
		keys = tuple(k for k in data)
		cursor = self.db.cursor()
		sql = "INSERT INTO {} {} VALUES {}".format(table_name, keys, tuple('%s' for _ in range(len(keys)))).replace("'", '')
		try:
			cursor.execute(sql, tuple(v for k,v in data.items()))
			self.db.commit()
			print(cursor.rowcount, "record inserted.")
		except Exception as e:
			print(e)

	# keys = ('name', "age")
	# val = [('name_value', 'age_value'), ('name_value', "ages_value")]
	def insert_multiple_rows(self,table_name, keys, val):
		cursor = self.db.cursor()
		sql = "INSERT INTO {} {} VALUES {}".format(table_name, keys, tuple('%s' for _ in range(len(keys)))).replace("'", "")
		try:
			cursor.executemany(sql, val)
			self.db.commit()
			print(cursor.rowcount, "was inserted.") 
		except Exception as e:
			print(e)

	# items = * or items = 'name', 'age'
	def find_all(self, table_name, items=None):
		cursor = self.db.cursor()
		if items :
			sql = "SELECT {} FROM {}".format(items, table_name).replace("'", "").replace('(', '').replace(')', '')
		else:
			sql = "SELECT * FROM {}".format(table_name)
		try:
			print(sql)
			cursor.execute(sql)
			return cursor.fetchall()
		except Exception as e:
			print(e)
			
	# filter = {"id" = 1}
	def find_one_by(self, table_name, **filter):
		key = [k for k in filter or []][0]
		if not key:
			key = 'id'
		cursor = self.db.cursor()		
		sql = "SELECT * FROM {} WHERE {} = %s".format(table_name, key)
		adr = (filter[key], )
		try:
			cursor.execute(sql, adr)
			return cursor.fetchone()
		except Exception as e:
			print(e)
			
	# filter = {"id" = 1}
	def find_by(self, table_name, **filter):
		key = [k for k in filter or []][0]
		if not key:
			key = 'id'
		cursor = self.db.cursor()		
		sql = "SELECT * FROM {} WHERE {} = %s".format(table_name, key)
		adr = (filter[key], )
		try:
			cursor.execute(sql, adr)
			return cursor.fetchall()
		except Exception as e:
			print(e)






#orm = DataBase('pythonScraping', "localhost", "root", "")
#from datetime import datetime
#orm.create_tabe("customers", ["age INT(255)", "description TEXT", "name VARCHAR(255)", "created_at DATETIME"])
#orm.insert_into_table("customers", age=12, description="coco les amis", name="Imad", created_at=datetime.now())

"""orm.insert_multiple_rows('customers', ('age', "description", 'name', 'created_at'),
	[
		(14, 'juste a nme', 'jamal', datetime.now()),
		(21, 'freind', 'kamal', datetime.now()),
		(25, 'lover', 'ayoub', datetime.now()),
		(19, 'champion', 'zakaria', datetime.now()),
		(22, 'smart', 'mohamed', datetime.now()),
	]
)
"""

#orm.find_all('customers')
#x = orm.find_one_by('customers', id=5)
