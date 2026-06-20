import mysql.connector  
import pandas as pd

connection= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="neobank"
)

print("Connected to NeoBank database!")

query="""
select transaction_id, customer_id, account, transaction_type,
transaction_time
from transactions where account>90000 order by account desc;
"""

df=pd.read_sql(query,connection)
print(df)
connection.close()