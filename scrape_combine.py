import ssl
import certifi
import pandas as pd
import sqlite3

# Override SSL verification to avoid certificate errors
ssl._create_default_https_context = ssl._create_unverified_context  

# Step 1: Scrape Data from Pro-Football-Reference
url = 'https://www.pro-football-reference.com/draft/2024-combine.htm'
tables = pd.read_html(url)
df = tables[0]  # Extract main table

# Step 2: Clean Column Names (Ensure compatibility with SQLite)
df.columns = [col.lower().replace(' ', '_').replace('%', 'percent') for col in df.columns]

# Step 3: Connect to SQLite Database
conn = sqlite3.connect('nfl_combine.db')

# Step 4: Store Data in SQLite (Replace Old Data)
df.to_sql('combine_results', conn, if_exists='replace', index=False)  # Replace ensures fresh data

conn.close()

print("Data successfully stored in SQLite!")
