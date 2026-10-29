import sqlite3
import os
import pandas as pd

# 1. Load CSV
df = pd.read_csv("D:\linkedin projects\job search engine\data\job_data_merged_1.csv")

# 2. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 3. Replace missing values
df = df.fillna("unknown")

# 4. Connect to database (create jobs.db file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "jobs.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 5. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    workplace TEXT,
    location TEXT,
    department TEXT,
    type TEXT
)
""")

# 6. Insert data
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO jobs (category, workplace, location, department, type)
    VALUES (?, ?, ?, ?, ?)
    """, (
        row["category"],
        row["workplace"],
        row["location"],
        row["department"],
        row["type"]
    ))

conn.commit()
conn.close()

print("Database created successfully!")