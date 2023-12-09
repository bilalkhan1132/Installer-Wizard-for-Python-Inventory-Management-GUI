import pandas as pd
import sqlite3

# Read Excel file
df = pd.read_excel('Components.xlsx')

# Create SQLite connection
conn = sqlite3.connect('components.db')

# Write DataFrame to SQLite database
df.to_sql('components_table', conn, index=False, if_exists='replace')

# Commit changes and close connection
conn.commit()
conn.close()
