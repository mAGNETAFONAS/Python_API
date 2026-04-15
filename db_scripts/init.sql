
USE web;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    surname VARCHAR(255),
    password VARCHAR(255),
    address VARCHAR(255),
    telephone_num VARCHAR(20),
    email VARCHAR(255)
);