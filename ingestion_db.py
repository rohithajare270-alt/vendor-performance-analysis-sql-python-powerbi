import pandas as pd

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Table '{table_name}' loaded successfully.")

