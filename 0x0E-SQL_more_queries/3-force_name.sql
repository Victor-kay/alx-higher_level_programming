-- Description: Create the 'force_name' table in the specified database.

USE your_database_name;  # Replace 'your_database_name' with the actual database name

-- Creating the table 'force_name' if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL  # 'name' field cannot be null
);
