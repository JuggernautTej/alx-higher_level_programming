-- Create database hbtn_0d_usa and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
id INT AUTO_INCREMENT UNIQUE NOT NULL,
PRIMARY KEY(id),
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256)
);
