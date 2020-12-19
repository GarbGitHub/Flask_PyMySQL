
DROP DATABASE IF EXISTS flask_mysql;
CREATE DATABASE flask_mysql;
USE flask_mysql;

   /* TABLE USERS */
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	user_id SERIAL PRIMARY KEY, 
    username varchar(100)
);

INSERT INTO users (username) VALUES
('mishunya'),
('kat'),
('sinior'),
('barmaleika'),
('dedushkinvnuchok'),
('golubmira'),
('maria'),
('serega'),
('38popugaew'),
('kibalchish');