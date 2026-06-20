select customer_id, max(transaction_time) as last_transaction
from transactions group by customer_id
order by last_transaction;