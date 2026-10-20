CREATE DATABASE IF NOT EXISTS harcama_db;
USE harcama_db;
CREATE TABLE harcamalar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    aciklama VARCHAR(255),
    kategori VARCHAR(50),
    tutar DECIMAL(10,2),
    tarih DATE
);
DESCRIBE harcamalar;

INSERT INTO harcamalar(aciklama, kategori, tutar, tarih_obj)
VALUES('Kahve', 'Yiyecek', 75, '2026-10-17');

SELECT*FROM harcamalar;



