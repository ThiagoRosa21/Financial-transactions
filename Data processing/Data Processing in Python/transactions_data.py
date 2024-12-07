import pandas as pd

csv_file = r"C:\Users\Thiago\Financial-transactions\Data processing\corrected_transactions_data2.csv"


df = pd.read_csv(csv_file)

df = df.where(pd.notnull(df), None)

df.columns = [col.replace("Soma de ", "") for col in df.columns]

inserts = []
for _, row in df.iterrows():
    values = []
    for value in row:
        if isinstance(value, str):  
            value = value.replace("'", "''") 
            values.append("'{}'".format(value))
        elif value is None:  
            values.append("NULL")
        else:  
            values.append(str(value))
    
    insert = "INSERT INTO {} ({}) VALUES ({});".format('TRANSACTIONS', ', '.join(df.columns), ', '.join(values))
    inserts.append(insert)

output_file = "Transactions.sql"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(inserts))

print(f"Inserts salvos em {output_file}")