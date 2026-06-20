from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
fake=Faker()
transactions=[]
for i in range(50000):
    transaction={
        "transaction_id": i+1,
        "customer_id":random.randint(1,5000),
        "amount":round(random.uniform(100,100000),2),
        "transaction_type":random.choice(
            ["transfer","deposit","withdrawal"]
         ),
         "transaction_time":fake.date_time_between(
             start_date="-1y",
             end_date="now"
         )

    }
    transactions.append(transaction)
df=pd.DataFrame(transactions)
df.to_csv("data/transactions.csv",index=False)
print("50,000 transactions created!")
