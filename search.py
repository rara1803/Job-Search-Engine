from database.database import (
    get_jobs_by_filters,
    get_unique_categories,
    get_unique_locations
)


def search_jobs(category=None, location=None, job_type=None, workplace=None, query=None):

    categories = [c.lower() for c in get_unique_categories()]
    locations = [l.lower() for l in get_unique_locations()]

    detected_categories = []
    detected_locations = []

    # -----------------------------
    # Smart parsing (order-independent)
    # -----------------------------
    if query:
        query = query.lower().strip()
        words = query.split()

        for word in words:

            # workplace
            if word in ["remote", "on-site", "hybrid"]:
                workplace = word
                continue

            # job type
            if word in ["full", "internship", "contract"]:
                job_type = "full time" if word == "full" else word
                continue

            # collect category matches
            for c in categories:
                if word in c:
                    detected_categories.append(c)

            # collect location matches
            for loc in locations:
                if word in loc:
                    detected_locations.append(loc)

        # assign AFTER processing all words
        if detected_categories:
            category = detected_categories[0]

        if detected_locations:
            location = detected_locations[0]

    # -----------------------------
    # Fetch results
    # -----------------------------
    jobs = get_jobs_by_filters(
        category=category,
        location=location,
        job_type=job_type,
        workplace=workplace
    )

    # -----------------------------
    # Ranking
    # -----------------------------
    ranked = []

    for job in jobs:
        score = 0
        _, job_category, job_workplace, job_location, _, job_type_db = job

        if category and category in job_category.lower():
            score += 4

        if location and location in job_location.lower():
            score += 3

        if job_type and job_type in job_type_db.lower():
            score += 2

        if workplace and workplace in job_workplace.lower():
            score += 2

        ranked.append((score, job))

    ranked.sort(reverse=True, key=lambda x: x[0])

    return [job for score, job in ranked]