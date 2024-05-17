# Create a function that converts csv files into a single sqlite database

# Your arguments should be
# path to csv files
# path to database
# database name

def create_database(csv_folder, database_path, database_name):
    """
    This function takes in the folder path to your csv files, and converts all the csv files
    inside that folder path and merges them into a single sqlite database

    Parameters:
    --------------------------------
    `csv_folder`: the path to the folder containing your csv files. If using mac, add an extra slash before your
    path to the folder containing the csv files. eg '/absolute/path/to/database". For windows users, no need to insert the extra slash.
    See this [reference](https://docs.sqlalchemy.org/en/20/core/engines.html)
    `database_path`: the path you would like to save your database into
    `database_name`: the name of your database eg database.db 
    """

    # Import the requisite packages
    from pathlib import Path
    import sqlite3
    import pandas as pd
    import glob
    import re
    from sqlalchemy import create_engine
    from sqlalchemy import inspect

    # Create the database from the provided path and concatenate it with the database name
    database_path_name = f"sqlite:///{database_path}/{database_name}.db"

    # Create database
    engine = create_engine(database_path_name)
    
    # database_path + database_name + ".db"
    # /home/sammigachuhi/github4/coding/sqlite_database/database/csv_data4.db

    # Create an engine from the path to the database concatenated above
    # First get the path to the csv files
    csv_path = csv_folder + "/"
    print(f"---csv_path:  {csv_path}------------")

    # Store the path to the csv files in a variable
    files = glob.glob(csv_folder + "/*.csv")

    # Create a for loop that iterates through the entire csv path, 
    # pick the csv files, and stores them into a database name provided 
    # by the database_name parameter above
    for i in files:
        # Lets first print the paths to each csv
        # print("\n--")
        # print(i)

        # Replace --- https://favtutor.com/blogs/replace-multiple-characters-in-string-python

        # We want to remove every path prior to the name of the csv and replace it with nothing.
        # This is so as to only print the name of the file.
        
        new_name = re.sub(csv_path, "", i)


        # Now assign the new names to every dataframe
        new_df = pd.read_csv(i)

        # Print each dataframe
        # print(f"\--Filename path: {i}")
        # print(new_df.head(2))

        table_name = new_name.replace(".csv", "")

        # Export the DataFrame to the SQLite database --- https://www.linkedin.com/pulse/exporting-pandas-data-frames-sqlite-sql-alchemy-skilgenie/
        new_df.to_sql(table_name, engine, if_exists='replace', index=False)

    # Now print the tables in your database
    print("\nThese are the tables in your database")
    inspector = inspect(engine)
    # print(inspector.get_table_names())

    for t in inspector.get_table_names():
        print(t)

create_database(
    # csv_folder="/home/sammigachuhi/github4/coding/sqlite_database/csv_files",
    csv_folder="/home/sammigachuhi/github4/csv_files",
                database_path="/home/sammigachuhi/github4/coding/sqlite_database/database",
                database_name="csv_data7") 


## Create function to read a table from database
print("\n---Function to read table from sqlite database-----")
def read_table_from_db(table_name, database_path):
    """
    This function takes in a table name and path to database and returns the first five rows of the dataframe from within that database.

    Parameters:
    -------------------------------
    `table_name`: This is the name of the table enclosed in quotes eg. "<table-name>"
    `database_path`: This is the full path to the database. Do not insert relative paths but rather the full path. If using mac, add an extra slash before your
    path to the folder to your database. eg '/absolute/path/to/database.db". For windows users, no need to insert the extra slash.
    See this [reference](https://docs.sqlalchemy.org/en/20/core/engines.html)
    """

    # Import requisite packages
    import pandas as pd
    from sqlalchemy import create_engine
    from sqlalchemy import inspect

    # Append database path with sqlite:/// prefix
    database_path = f"sqlite:///{database_path}"

    # Create database engine
    connection = create_engine(database_path)

    # Read the table from sqlite database
    table = pd.read_sql_table(
        table_name=table_name,
        con=connection
    )

    # Returns the first 5 rows of the table read from the sqlite database
    print(table.head(5))

read_table_from_db("mock_sensor_operation_table", "/home/sammigachuhi/github4/coding/sqlite_database/database/csv_data7.db")