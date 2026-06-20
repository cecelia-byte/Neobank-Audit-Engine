-- select count(*) as total
-- from neobank.transactions;
-- select transaction_type, count(*) as total FROM transactions
-- group by transaction_type;
-- select customer_id, sum(account) as total_money_moved
-- from transactions group by customer_id order by total_money_moved desc limit 10;
-- DESCRIBE transactions;

-- select * from transactions order by account desc limit 10;

-- select transaction_id, customer_id, account, transaction_type, transaction_time from transactions
-- where account> 90000 order by account desc;

-- select customer_id, count(*) as transaction_count from transactions 
-- group by customer_id having count(*)>20 order by transaction_count desc;

select transaction_id, customer_id, account, transaction_time from transactions
where hour(transaction_time) between 0 and 5 
order by transaction_time;