from flask import Flask, render_template, request, jsonify
from search import search_jobs
from database.database import get_unique_countries, get_unique_categories, get_connection, insert_job

app = Flask(__name__)


@app.route("/")
def home():
    countries = get_unique_countries()
    categories = get_unique_categories()
    return render_template("index.html", countries=countries, categories=categories)


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    jobs = search_jobs(
        query=data.get("query"),
        category=data.get("category"),
        location=data.get("location"),
        job_type=data.get("job_type"),
        workplace=data.get("workplace")
    )
    return jsonify(jobs)


@app.route("/locations")
def locations():
    conn = get_connection()
    rows = conn.execute(
        "SELECT DISTINCT location FROM jobs WHERE location IS NOT NULL ORDER BY location"
    ).fetchall()
    conn.close()

    countries = set()
    for row in rows:
        loc = row[0]
        if loc:
            # take only the last part after the final comma
            country = loc.split(",")[-1].strip()
            if country:
                countries.add(country)

    return jsonify(sorted(list(countries)))


@app.route("/count")
def count():
    conn = get_connection()
    row = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()
    conn.close()
    return jsonify({"count": row[0]})


@app.route("/post-job", methods=["POST"])
def post_job():
    data = request.get_json()
    insert_job(
        data.get("category"),
        data.get("workplace"),
        data.get("location"),
        data.get("department"),
        data.get("job_type")
    )
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
