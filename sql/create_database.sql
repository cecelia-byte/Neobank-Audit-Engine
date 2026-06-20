-- create database neobank;
use neobank;
create table transactions(
    transaction_id int primary key,
    customer_id int,
    account decimal(10,2),
    transaction_type varchar(20),
    transaction_time DATETIME
);