DROP DATABASE restaurant_service;
CREATE DATABASE restaurant_service DEFAULT CHARACTER SET utf8;

USE restaurant_service;

CREATE TABLE IF NOT EXISTS restaurant(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    region VARCHAR(100),
    Tel VARCHAR(100),
    PRIMARY KEY(id)
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS detail(
    id INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(255),
    address VARCHAR(255),
    opentime VARCHAR(200),
    restaurant_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS images(
    id INT NOT NULL AUTO_INCREMENT,
    image VARCHAR(255),
    restaurant_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
) DEFAULT CHARSET=utf8;
