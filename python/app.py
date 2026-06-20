import streamlit as st
import mysql.connector
import pandas as pd

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="neobank"
)
query= """
select 
transaction_id,
customer_id,
account,
transaction_type,
transaction_time from transactions 
where account>90000;
"""
df=pd.read_sql(query,connection)
st.title("NeoBank Fraud Detection Dashboard")
st.write("Suspicious High Value Transactions")
st.dataframe(df)
st.subheader("Fraud Summary")
col1,col2= st.columns(2)

if df.empty:
    st.warning("No transactions found matching your search.")
else:
    st.write(df)


with col1:
    st.metric(
        "Suspicious Transactions",
        len(df)
    )

with col2:
    st.metric(
        "Total amount Flagged",
        df["account"].sum()
    )

st.subheader("Transaction Type Distribution")
type_count= df["transaction_type"].value_counts()
st.bar_chart(type_count)

# 1. Apply the transaction type filter first (if selected)
transaction_filter = st.multiselect("Filter by Transaction Type", options=df["transaction_type"].unique())
if transaction_filter:
    df = df[df["transaction_type"].isin(transaction_filter)]

# 2. Apply the search query filter on top of the already filtered data
search_query = st.text_input("Search for a Customer ID")
if search_query:
    df = df[df['customer_id'].astype(str).str.contains(search_query, na=False)]

# 3. Display the final result
st.write(df)

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Fraud Report as CSV",
    data=csv,
    file_name='fraud_report.csv',
    mime='text/csv',
)
connection.close()

