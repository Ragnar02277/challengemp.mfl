-- Create the database (adjust the name as per your preference)
CREATE DATABASE IF NOT EXISTS MyDatabase;
USE MyDatabase;

-- Create the Manager table
CREATE TABLE Manager (
    id_manager INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Create the Owner table
CREATE TABLE Owner (
    id_owner INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Manager(id_manager)
);

-- Create the DatabaseInfo table
CREATE TABLE DatabaseInfo (
    id_database INT PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    classification ENUM('High', 'Medium', 'Low') NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES Owner(id_owner)
);