from sqlalchemy import Table, Column, Integer, Float, String, create_engine, MetaData

class MyDatabase:
	DB_ENGINE = {"sqlite" : "sqlite:///{DB}"}
	db_engine = None

	def __init__(self, dbtype, dbname=''):
		dbtype = dbtype.lower()

		if dbtype in self.DB_ENGINE.keys():
			engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
			self.db_engine = create_engine(engine_url)
			print(self.db_engine)
		else:
			print("DBTYPE is not found in DB_ENGINE")

	def pandas_to_table(self, dataframe = None, table_name=''):
		try:
			dataframe.to_sql(table_name, con=self.db_engine, if_exists='replace')
		except Exception as e:
			print(e)

	def create_db_table(self, table_name):
		"""
		Creates a new table in database with a given name
		Parameters
		----------
		table_name : str
			Name for new table

		Returns
		-------
		Executes SQLITE3 query to generate a new table with default columns 'id' and 'Name'
		"""

		metadata = MetaData()
		table = Table(table_name, metadata,
					Column('id', Integer, primary_key=True),
					Column('Name', String))

		try:
			metadata.create_all(self.db_engine)
		except Exception as e:
			print("Error occurred during Table creation :(")
			print(e)

	def execute_query(self, query=''):
		"""
		Execute given SQLITE3 Query
		Parameters
		----------
		query : str
			Query to execute

		Returns
		-------
			Executes given query
		"""

		if query == '' : return
		print(query)

		with self.db_engine.connect() as conn:
			try:
				result = conn.execute(query)
			except Exception as e:
				print(e)

			else:
				for row in result:
					print(row)
				result.close()

	def add_col(self, table_name, col_name, dtype):
		"""
		Add a new column to an existing table
		Parameters
		----------
		table_name : Name of table to edit
		col_name : Name of new column to create
		dtype : Data type of the new column

		Returns
		-------
		Executes SQLITE3 query to alter table_name
		"""

		with self.db_engine.connect() as conn:
			if type(col_name) == 'str':  # In the case where one column is created
				col_name = [col_name]
				dtype = [dtype]

			for col, d in zip(col_name, dtype):
				try:
					command = "ALTER TABLE '{table_name}' ADD '{col_name}' '{dtype}'"
					sql_command = command.format(table_name=table_name,
												 col_name=col,
												 dtype=d)
					conn.execute(sql_command)
				except Exception as e:
					print(e)
					continue

	def insert(self, table, columns, values):
		query = "INSERT INTO '{table}' ('{columns}') " \
				"VALUES ('{values}')".format(table=table,
										   columns=columns,
										   values=values)
		self.execute_query(query)
		self.print_all_data(table)

	def print_all_data(self, table='', query=''):
		query = query if query != '' else "SELECT * FROM '{}';".format(table)
		print(query)

		with self.db_engine.connect() as conn:
			try:
				result = conn.execute(query)
			except Exception as e:
				print(e)
			else:
				for row in result:
					print(row)
				result.close()
			print("\n")
