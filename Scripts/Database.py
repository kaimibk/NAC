from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Float, String, create_engine, MetaData

obj_name = "Pleiades"

Base = declarative_base()

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


	def create_db_table(self, table_name):
		"""
		Creates a new table in database with a given name
		Parameters
		----------
		table_name : str
			Name for new table

		Returns
		-------
		Executes SQLITE3 query to generate a new table
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
				conn.execute(query)
			except Exception as e:
				print(e)

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

			for col, d in zip([col_name], [dtype]):
				try:
					command = "ALTER TABLE '{table_name}' ADD '{col_name}' '{dtype}'"
					sql_command = command.format(table_name=table_name,
												 col_name=col,
												 dtype=d)
					conn.execute(sql_command)
				except Exception as e:
					print(e)
					continue


	# class Star(Base):
	#
	#     id = Column(Integer, primary_key=True)
	#     name = Column(String)
	#     ra = Column(String)
	#     dec = Column(String)
	#
	#     parallax = Column(Float)
	#
	#     radius_val = Column(Float)
	#     radius_percentile_lower = Column(Float)
	#     radius_percentile_upper = Column(Float)
	#     radius_err = Column(Float)
	#
	#     lum_val = Column(Float)
	#     lum_percentile_lower = Column(Float)
	#     lum_percentile_upper = Column(Float)
	#     lum_err = Column(Float)
	#
	#     teff_val = Column(Float)
	#     teff_percentile_lower = Column(Float)
	#     teff_percentile_upper = Column(Float)
	#
	#     def __init__(self, tablename, name):
	#         self.__tablename__ = tablename
	#         self.name = name
	#
	#     def __repr__(self):
	#         return "<Star(name = '%s')>" % (self.name)




	# class Jackson(Base):
	#
	#     __tablename__ = "Jackson"
	#     id = Column(Integer, primary_key=True)
	#     name = Column(String)
	#     ra = Column(String)
	#     dec = Column(String)
	#
	#     K2MASS = Column(Float)
	#     V_Ko = Column(Float)
	#     Period = Column(Float)
	#     BCK = Column(Float)
	#     logL_Lo = Column(Float)
	#     M_Mo = Column(Float)
	#     R_Ro = Column(Float)
	#     vsinip = Column(Float)
	#     MK = Column(Float)
	#     LogL_Lo_y = Column(Float)
	#     SNR = Column(Float)
	#     RV = Column(Float)
	#     SRV = Column(Float)
	#     FWHM = Column(Float)
	#     SFWHM = Column(Float)
	#     FWHMo = Column(Float)
	#     VSINI = Column(String)
	#     EVSINI = Column(Float)
	#     Rsini = Column(String)
	#
	#     def __repr__(self):
	#         return "<Star(name = '%s')>" % (self.name)

	#test_star = Gaia(name='Star1', ra="0.000", dec="0.000")
	#test_star = Star(tablename='Gaia', name='Test1')