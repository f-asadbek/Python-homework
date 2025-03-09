import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

# Define the job listings URL
URL = "https://realpython.github.io/fake-jobs"

def fetch_jobs():
    """Scrape job listings from the website."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching jobs: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_card in soup.find_all("div", class_="card-content"):
        title = job_card.find("h2", class_="title").text.strip()
        company = job_card.find("h3", class_="company").text.strip()
        location = job_card.find("p", class_="location").text.strip()

        # Ensure description exists before accessing `.text`
        description_tag = job_card.find("div", class_="description")
        description = description_tag.text.strip() if description_tag else "No description available"

        # Ensure link exists
        link_tag = job_card.find("a", text="Apply")
        link = link_tag["href"] if link_tag else "No link available"

        jobs.append((title, company, location, description, link))

    return jobs

def setup_database():
    """Create the SQLite database and jobs table if they don't exist."""
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                link TEXT,
                UNIQUE(title, company, location)
            )
        ''')
        conn.commit()

def insert_jobs(jobs):
    """Insert job listings into the database, avoiding duplicates."""
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        for job in jobs:
            cursor.execute('''
                INSERT OR IGNORE INTO jobs (title, company, location, description, link)
                VALUES (?, ?, ?, ?, ?)
            ''', job)
        conn.commit()

def update_jobs(jobs):
    """Update job listings if the description or link has changed."""
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()

        for job in jobs:
            title, company, location, description, link = job
            cursor.execute('''
                SELECT description, link FROM jobs
                WHERE title = ? AND company = ? AND location = ?
            ''', (title, company, location))
            
            result = cursor.fetchone()
            if result and (result[0] != description or result[1] != link):
                cursor.execute('''
                    UPDATE jobs
                    SET description = ?, link = ?
                    WHERE title = ? AND company = ? AND location = ?
                ''', (description, link, title, company, location))

        conn.commit()

def filter_jobs(filter_by, value):
    """Retrieve jobs based on location or company name."""
    with sqlite3.connect("jobs.db") as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM jobs WHERE {filter_by} = ?"
        cursor.execute(query, (value,))
        results = cursor.fetchall()
    return results

def export_to_csv(filename="jobs.csv"):
    """Export job listings to a CSV file."""
    with sqlite3.connect("jobs.db") as conn, open(filename, "w", newline="", encoding="utf-8") as file:
        cursor = conn.cursor()
        cursor.execute("SELECT title, company, location, description, link FROM jobs")
        jobs = cursor.fetchall()
    
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Job Description", "Application Link"])
        writer.writerows(jobs)

if __name__ == "__main__":
    setup_database()
    job_listings = fetch_jobs()
    if job_listings:
        insert_jobs(job_listings)
        update_jobs(job_listings)
        print("Job listings updated successfully!")
    else:
        print("No job listings found.")
