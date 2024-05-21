from cd_to_db_converter import create_database
from cd_to_db_converter import read_table_from_db

create_database(
    csv_folder="csv_files",
    database_path="database",
    database_name="test"
)

read_table_from_db(
    table_name="mock_project_metrics",
    database_path="database/test.db"
)