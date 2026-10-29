from database.database import get_jobs_by_filters, get_unique_categories, get_unique_locations
from search import search_jobs

def run():
    print("=== Job Search Engine ===")

    print("\nExample values:")
    print("Workplace: Remote, On-site, Hybrid")
    print("Type: Full time, Internship, Contract\n")
    print("Categories:")
    for c in get_unique_categories():
        print("-", c)
    print("\nLocations:")
    for l in get_unique_locations():
        print("-", l)
    print()

    query = input("Search jobs: ")

    jobs = search_jobs(query=query)

    print("\nResults:\n")

    if not jobs:
        print("No matching job offers available.\n")
    else:
        for job in jobs[:10]:
            id, category, workplace, location, department, job_type = job

            print(f"""
    Job ID: {id}
    Role: {category}
    Location: {location}
    Workplace: {workplace}
    Type: {job_type}
    Department: {department}
    -------------------------
    """)

if __name__ == "__main__":
    run()
