# Create database
from pathlib import Path
import sqlite3
import pandas as pd
import glob
import re
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import Table
from sqlalchemy import MetaData

# Path("../database/csv_data.db").touch()
# Path("../database/csv_data2.db").touch() # For the for loop

# database = "../database/csv_data.db"
# database2 = "../database/csv_data2.db" # For the for loop

# Create a database connection
# conn = sqlite3.connect(database)
# conn = sqlite3.connect(database2) # For the for loop
# c = conn.cursor()

# Replace 'mydatabase.db' with your desired database name
engine = create_engine('sqlite:////home/sammigachuhi/github4/coding/sqlite_database/database/csv_data4.db')

# Load the csv into sqlite


# Create a for loop that iterates through all the csv files and stores them in a single database
csv_path = "../csv_files"
files = glob.glob(csv_path + "/*.csv")

for i in files:
    # Lets first print the paths to each csv
    print("\n--")
    print(i)

    # Replace --- https://favtutor.com/blogs/replace-multiple-characters-in-string-python
    new_name = re.sub("../csv_files/|.csv|\s", "", i)
    print(new_name)

    # Table names with strings
    table_name = f"'{new_name}'"
    print(f"---{table_name}---")

    # Now assign the new names to every dataframe
    new_df = pd.read_csv(i)

    # Print each dataframe
    print(f"\--Filename path: {i}")
    print(new_df.head(2))

    # if new_name == table_name:
    # Export the DataFrame to the SQLite database --- https://www.linkedin.com/pulse/exporting-pandas-data-frames-sqlite-sql-alchemy-skilgenie/
    new_df.to_sql(new_name, engine, if_exists='replace', index=False)


# Query data from the SQLite database
# query = "SELECT * FROM 'mock_sensor_operation_table'"
# result_df = pd.read_sql(query, engine)
# print(result_df)

# List the existing tables in your database --- https://stackoverflow.com/questions/6473925/sqlalchemy-getting-a-list-of-tables
print("\n------------table names------------")
inspector = inspect(engine)
print(inspector.get_table_names())

# Print a particular table
# metadata = MetaData()

# mock_sensor_operation_table = Table('mock_sensor_operation_table', metadata, autoload_with=engine)

# # Print the column names
# print("\n---column names----")
# print(mock_sensor_operation_table.columns.keys())


# # Print full table metadata
# print("\n---full metadata---")
# print(repr(metadata.tables['mock_sensor_operation_table']))

print("\n----a particular table----") # --- https://www.geeksforgeeks.org/read-sql-database-table-into-a-pandas-dataframe-using-sqlalchemy/
# cnx = create_engine('sqlite:////home/sammigachuhi/github4/coding/sqlite_database/database/csv_data4.db').connect()
# mock_sensor_operation_table = pd.read_sql_table(
#     "mock_sensor_operation_table",
#     cnx
# )

mock_sensor_operation_table = pd.read_sql_table(
    "mock_sensor_operation_table",
    engine
)

print(mock_sensor_operation_table)
