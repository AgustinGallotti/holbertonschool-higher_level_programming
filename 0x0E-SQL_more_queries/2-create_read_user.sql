-- sql
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
