# Create database
from pathlib import Path
import sqlite3
import pandas as pd
import glob

Path("../database/csv_data.db").touch()
# Path("../database/csv_data2.db").touch() # For the for loop

database = "../database/csv_data.db"
# database2 = "../database/csv_data2.db" # For the for loop

# Create a database connection
conn = sqlite3.connect(database)
# conn = sqlite3.connect(database2) # For the for loop
c = conn.cursor()

# Load the csv into sqlite
mock_birdnet_observations = pd.read_csv("../csv_files/mock_birdnet_observations.csv")
mock_birdnet_observations.to_sql("mock_birdnet_observations", conn,
                                 if_exists="replace", index=False)


mock_project_dendrogram = pd.read_csv("../csv_files/mock_project_dendrogram.csv")
mock_project_dendrogram.to_sql("mock_project_dendrogram", conn,
                                 if_exists="replace", index=False)

mock_project_metrics = pd.read_csv("../csv_files/mock_project_metrics.csv")
mock_project_metrics.to_sql("mock_project_metrics", conn,
                                 if_exists="replace", index=False)

mock_project_timeline = pd.read_csv("../csv_files/mock_project_timeline.csv")
mock_project_timeline.to_sql("mock_project_timeline", conn,
                                 if_exists="replace", index=False)

mock_raw_deployments = pd.read_csv("../csv_files/mock_raw_deployments.csv")
mock_raw_deployments.to_sql("mock_raw_deployments", conn,
                                 if_exists="replace", index=False)

mock_raw_observations = pd.read_csv("../csv_files/mock_raw_observations.csv")
mock_raw_observations.to_sql("mock_raw_observations", conn,
                                 if_exists="replace", index=False)

mock_rbs_acoustic_covariates = pd.read_csv("../csv_files/mock_rbs_acoustic_covariates.csv")
mock_rbs_acoustic_covariates.to_sql("mock_rbs_acoustic_covariates", conn,
                                 if_exists="replace", index=False)

mock_sensor_operation_table = pd.read_csv("../csv_files/mock_sensor_operation_table.csv")
mock_sensor_operation_table.to_sql("mock_sensor_operation_table", conn,
                                 if_exists="replace", index=False)

mock_site_covs = pd.read_csv("../csv_files/mock_site_covs.csv")
mock_site_covs.to_sql("mock_site_covs", conn,
                                 if_exists="replace", index=False)

# Create a for loop that iterates through all the csv files and stores them in a single database
# csv_path = "../csv_files"
# files = glob.glob(csv_path + "/*.csv")

# for i in files:
    # i = pd.read_csv(i)
    # # print(i)
    # i.to_sql(i, conn, if_exists="replace", index=False)
    # dataframes = []
    # i == pd.read_csv(i)
    # # print(i)
    # dataframes.append(i)
    # for j in dataframes:
    #     j.to_sql(j, conn, if_exists="replace", index=False)
    # # i == i.replace(".csv", "")
    # # print(i)
    # # i.to_sql(i, conn, if_exists="replace", index=False)



# Fetch values from sqlite table
test = c.execute(
    '''
SELECT * FROM mock_sensor_operation_table
'''
).fetchall()

print(test)

print("\n-------------------\n")
test2 = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(test2.fetchall())

print("\n------------------------------------------\n")
test3 = pd.read_sql('''SELECT * FROM mock_sensor_operation_table''', conn)
print(test3)