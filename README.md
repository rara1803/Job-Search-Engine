# OOB — Outside of the Box | Job Search Engine

A Python-based job search engine that helps users explore job opportunities through keyword searches, customizable filters, and rule-based relevance ranking.

Built with **Python, Flask, SQLite, HTML, CSS, and JavaScript**, this project demonstrates how data structures, search algorithms, and database operations can be combined to create a practical web application.

## Features

- **Keyword Search:** Find job listings based on search queries.
- **Advanced Filtering:** Filter jobs by location, category, job type, and workplace arrangement.
- **Job Ranking:** Sort matching jobs using a rule-based scoring algorithm.
- **Interactive Web Interface:** Browse job listings through a Flask-powered website.
- **Database Integration:** Retrieve and filter job listings stored in SQLite.

## Screenshots

### Homepage
![Homepage](screenshots/OOB-frontpage.png)

### Job Search
![Job Search Results](screenshots/OOB-filtering-system.png)

### Filtering System
![Job Search Results](screenshots/OOB-filtering-system.png)

## Data Structures & Algorithms

The search engine applies fundamental Python data structures and algorithms:

| Concept | Implementation |
|---|---|
| **Lists** | Store matching keywords and search results. |
| **Tuples** | Associate job records with relevance scores. |
| **Dictionaries** | Handle search parameters and job information. |
| **String Processing** | Extract and match keywords from search queries. |
| **Sorting** | Order job listings based on calculated relevance scores. |

The ranking algorithm assigns scores based on matching job categories, locations, job types, and workplace arrangements.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** pandas

## Installation & Setup

### Requirements

- Python 3
- PyCharm (or another Python IDE)
- Flask and pandas

### 1. Download the Project

1. Click the green **Code** button on this repository.
2. Select **Download ZIP**.
3. Extract the ZIP file.
4. Open the extracted project folder in PyCharm.

### 2. Install Dependencies

Make sure Python is configured as your project's interpreter in PyCharm.

Install the required packages using **Settings → Project → Python Interpreter → + (Install Package)**:

- `Flask`
- `pandas`

These dependencies are also listed in `requirements.txt`.

### 3. Initialize the Database

The application uses a CSV dataset to populate its SQLite database.

1. Open `backend/database/init_db.py`.
2. Update the CSV file path to point to `data/job_data_merged_1.csv` on your computer.
3. Right-click `init_db.py` and select **Run 'init_db'**.

This creates and populates the local SQLite database.

**Note:** The current initialization script contains a machine-specific file path that must be updated before running it on another computer.

### 4. Run the Application

1. Open `backend/website/app.py` in PyCharm.
2. Make sure the `backend` folder is configured as a source root so Python can find the project's modules.
3. Right-click inside the file and select **Run 'app'**, or click the green **Run ▶** button.
4. Once Flask starts, open the following address in your browser:

`http://127.0.0.1:5000`

The OOB Job Search Engine website should now be accessible locally.

## Project Structure

```text
job-search-engine/
├── backend/
│   ├── main.py
│   ├── search.py
│   ├── database/
│   │   ├── database.py
│   │   └── init_db.py
│   └── website/
│       ├── app.py
│       └── templates/
│           └── index.html
├── data/
│   └── job_data_merged_1.csv
├── screenshots/
│   ├── homepage.png
│   └── search-results.png
├── requirements.txt
└── README.md
```

## Dataset Limitations

The project uses a limited job listings dataset, which means the available job categories, locations, and employment types are currently restricted to the options included in the dataset.

The search engine can be expanded to support a wider variety of opportunities by integrating larger datasets or live job listing APIs.

## Future Improvements

- **Job Posting:** Complete the existing "Post a Job" feature so users can submit new job listings directly through the website.
- **Smarter Search:** Improve keyword matching and explore NLP-based semantic search.
- **Database Improvements:** Simplify database initialization and improve data handling.
- **Deployment:** Host the application online to make it publicly accessible.
