CREATE DATABASE IF NOT EXISTS counterdb;

USE counterdb;

CREATE TABLE IF NOT EXISTS counter (
    id INT PRIMARY KEY,
    value INT
);

INSERT INTO counter (id, value) VALUES (1, 0)
ON DUPLICATE KEY UPDATE value = value;
