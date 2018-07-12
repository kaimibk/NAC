from Database import MyDatabase
import pandas as pd

main_dir = "/u/kaimibk/Documents/Research/NAC/"
data_dir = main_dir+"data/"
out_dir = main_dir+"output/"

def main():
	df = pd.read_csv(data_dir + "MN_17_3616_point.csv", index_col=0)

	table_name = 'GAIA'
	dbms = MyDatabase(dbtype='sqlite', dbname='/u/kaimibk/Documents/Git/NAC/Pleiades.db')
	dbms.pandas_to_table(dataframe=df, table_name=table_name)

	dbms.print_all_data(table=table_name)
	#dbms.create_db_table(table_name=table_name)

	#dbms.add_col(table_name=table_name, col_name=list(df.columns), dtype=["TEXT"]*len(df.columns))



if __name__ == "__main__":
	main()
