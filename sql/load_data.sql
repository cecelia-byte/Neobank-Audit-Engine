USE neobank;
LOAD DATA LOCAL INFILE 'C:/Users/Lenovo/Desktop/Neobank-Audit-Engine/data/transactions.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;