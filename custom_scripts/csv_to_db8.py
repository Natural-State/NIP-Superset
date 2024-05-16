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
    csv_folder: the path to the folder containing your csv files
    database_path: the path you would like to save your database into
    database_name: the name of your database eg database.db 
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
        print("\n--")
        print(i)

        # Replace --- https://favtutor.com/blogs/replace-multiple-characters-in-string-python

        # We want to remove every path prior to the name of the csv and replace it with nothing.
        # This is so as to only print the name of the file.
        
        new_name = re.sub(csv_path, "", i)


        # Now assign the new names to every dataframe
        new_df = pd.read_csv(i)

        # Print each dataframe
        print(f"\--Filename path: {i}")
        print(new_df.head(2))

        table_name = new_name.replace(".csv", "")

        # Export the DataFrame to the SQLite database --- https://www.linkedin.com/pulse/exporting-pandas-data-frames-sqlite-sql-alchemy-skilgenie/
        new_df.to_sql(table_name, engine, if_exists='replace', index=False)

    # Now print the tables in your database
    print("\nThese are the tables in your database")
    inspector = inspect(engine)
    print(inspector.get_table_names())

#     for t in inspector.get_table_names():
#         print(t)

create_database(csv_folder="/home/sammigachuhi/github4/coding/sqlite_database/csv_files",
                database_path="/home/sammigachuhi/github4/coding/sqlite_database/database",
                database_name="csv_data6") 

# # Print one of the tables to check if the function is working
# from sqlalchemy import create_engine
# from sqlalchemy import inspect
# import pandas as pd
# cnx = create_engine("sqlite:////home/sammigachuhi/github4/coding/sqlite_database/database/csv_data6.db").connect() # Replace with path to your database, add sqlite://// to path name
# mock_sensor_operation_table = pd.read_sql_table(
#     table_name="mock_sensor_operation_table",
#     con=cnx
# )

# print(mock_sensor_operation_table)