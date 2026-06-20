select customer_id, sum(account) as total_spent, count(*) as number_of_transactions FROM 
transactions group by customer_id order by total_spent DESC limit 10;