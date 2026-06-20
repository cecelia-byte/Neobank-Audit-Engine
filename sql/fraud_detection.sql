use neobank;
-- select customer_id, count(*) as total_transactions from transactions where transaction_type='transfer'
-- group by customer_id having count(*)>20;
-- select customer_id, count(*) as total_transactions from transactions where transaction_type='transfer' group by customer_id
-- having count(*)>5;

-- high value transactions
select transaction_id, customer_id, account, transaction_type, transaction_time from transactions
where account> 90000 order by account desc;

-- high transaction frequency
select customer_id, count(*) as transaction_count from transactions 
group by customer_id having count(*)>20 order by transaction_count desc;


-- odd transaction timing
select transaction_id, customer_id, account, transaction_time from transactions
where hour(transaction_time) between 0 and 5 
order by transaction_time;