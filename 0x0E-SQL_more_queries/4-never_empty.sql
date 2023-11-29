USE your_database_name; -- Replace 'your_database_name' with your actual database name

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
