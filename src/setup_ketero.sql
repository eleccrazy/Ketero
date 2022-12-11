CREATE DATABASE IF NOT EXISTS ketero_db;
CREATE USER IF NOT EXISTS 'ketero_user'@'localhost' IDENTIFIED BY 'ketero';
GRANT ALL PRIVILEGES ON `ketero_db`.* TO 'ketero_user'@'localhost';
FLUSH PRIVILEGES;
