import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "jobs.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_jobs_by_filters(category=None, location=None, job_type=None, workplace=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if category:
        query += " AND LOWER(category) LIKE LOWER(?)"
        params.append(f"%{category}%")

    if location:
        query += " AND LOWER(location) LIKE LOWER(?)"
        params.append(f"%{location}%")

    if job_type:
        query += " AND LOWER(type) LIKE LOWER(?)"
        params.append(f"%{job_type}%")

    if workplace:
        query += " AND LOWER(workplace) LIKE LOWER(?)"
        params.append(f"%{workplace}%")

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results


def get_unique_categories():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT category FROM jobs")
    result = [row[0] for row in cursor.fetchall()]
    conn.close()
    return result


def get_unique_locations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT location FROM jobs")
    result = [row[0] for row in cursor.fetchall()]
    conn.close()
    return result


def suggest_locations(prefix):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT location
        FROM jobs
        WHERE LOWER(location) LIKE LOWER(?)
        LIMIT 10
    """, (prefix + '%',))
    results = [row[0] for row in cursor.fetchall()]
    conn.close()
    return results


def get_unique_countries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT location FROM jobs")
    rows = cursor.fetchall()
    countries = set()
    for row in rows:
        location = row[0]
        if location and "," in location:
            country = location.split(",")[-1].strip()
            countries.add(country)
        else:
            countries.add(location)
    conn.close()
    return sorted(list(countries))


def insert_job(category, workplace, location, department, job_type):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        INSERT INTO jobs (category, workplace, location, department, job_type)
        VALUES (?, ?, ?, ?, ?)
    """, (category, workplace, location, department, job_type))
    conn.commit()
    conn.close()
