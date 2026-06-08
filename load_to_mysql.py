import pandas as pd
import pymysql


con = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="sql123",
    database="BoomTown",
)



cursor = con.cursor()

df = pd.read_csv("Combined_Record/combined_expenses.csv")

print("Rows to insert:", len(df))

for index, row in df.iterrows():

    
    cursor.execute("""
        INSERT INTO expenses (project_id, department, amount, expense_date)
        VALUES (%s, %s, %s, %s)
    """, (
        row['project_id'],
        row['department'],
        row['amount'],
        row['date']
    ))

con.commit()

print("Data inserted successfully!")

cursor.close()
con.close()