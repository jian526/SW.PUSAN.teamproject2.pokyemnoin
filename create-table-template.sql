CREATE DATABASE myproject
    DEFAULT CHARACTER SET = 'utf8mb4';
USE myproject;

CREATE TABLE heatwave_shelters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    address TEXT,
    latitude DOUBLE,
    longitude DOUBLE,
    capacity INT,
    weekday_open TIME,
    weekday_close TIME,
    weekend_open TIME,
    weekend_close TIME,
    member_only BOOLEAN
);
SELECT * FROM heatwave_shelters LIMIT 100;

CREATE TABLE weather_forecast (
    id INT AUTO_INCREMENT PRIMARY KEY,
    base_date DATE,
    base_time TIME,
    fcst_date DATE,
    fcst_time TIME,
    category VARCHAR(10),
    value VARCHAR(10),
    nx INT,
    ny INT
);

SELECT * FROM heatwave_shelters LIMIT 100;
