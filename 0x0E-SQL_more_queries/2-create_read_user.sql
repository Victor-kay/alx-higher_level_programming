-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'%' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege in hbtn_0d_2 to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'%';

-- Reload the privileges to apply the changes
FLUSH PRIVILEGES;
