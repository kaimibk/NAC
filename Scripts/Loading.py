from Database import MyDatabase

def main():
    table_name = 'GAIA'
    dbms = MyDatabase(dbtype='sqlite', dbname='/u/kaimibk/Documents/Pleiades.db')
    dbms.create_db_table(table_name=table_name)


    dbms.add_col(table_name=table_name, col_name='RA', dtype = "TEXT")
    dbms.add_col(table_name=table_name, col_name='Dec', dtype="TEXT")
    dbms.add_col(table_name=table_name, col_name='Test', dtype="TEXT")

if __name__ == "__main__":
    main()