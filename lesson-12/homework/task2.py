import sqlite3
import requests
from bs4 import BeautifulSoup
import csv

def fetch_jobs():
    url = 'https://realpython.github.io/fake-jobs'
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    job_listings = []
    for job in soup.find_all('div', class_='card-content'):
        title = job.find('h2').text
        company = job.find('h3').text
        location = job.find('p', class_='location').text.strip()
        description = job.find('div', class_='content').text.strip()
        application_link = job.find('a', class_='card-footer-item')['href']
        job_listings.append([title, company, location, description, application_link])
    return job_listings

def db_init():
    with sqlite3.connect('jobs.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS jobs")
        cursor.execute("""
        CREATE TABLE jobs (
            Job_Title TEXT,
            Company_Name TEXT,
            Location TEXT,
            Job_Description TEXT,
            Application_Link TEXT,
            PRIMARY KEY (Job_Title, Company_Name, Location)
        )
        """)
        conn.commit()

def save_to_db(jobs):
    with sqlite3.connect('jobs.db') as conn:
        cursor = conn.cursor()
        for job in jobs:
            cursor.execute("""
                INSERT INTO jobs (Job_Title, Company_Name, Location, Job_Description, Application_Link)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(Job_Title, Company_Name, Location)
                DO UPDATE SET
                    Job_Description = excluded.Job_Description,
                    Application_Link = excluded.Application_Link
                """, job)
        conn.commit()

def filter_jobs(Company_Name=None, Location=None):
    with sqlite3.connect('jobs.db') as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM jobs WHERE 1=1'
        params = []
        if Company_Name:
            query += ' AND Company_Name LIKE ?'
            params.append(f"%{Company_Name}%")
        if Location:
            query += ' AND Location LIKE ?'
            params.append(f"%{Location}%")
        cursor.execute(query, params)
        return cursor.fetchall()

def exp_to_csv(filtered_jobs, filename='filtered_jobs.csv'):
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Job_Title', 'Company_Name', 'Location', 'Job_Description', 'Application_Link'])
        writer.writerows(filtered_jobs)
    print(f"Filtered jobs saved to {filename}")

if __name__ == '__main__':
    db_init()
    jobs = fetch_jobs()
    save_to_db(jobs)
    print("Jobs updated successfully!")
    filtered_jobs = filter_jobs(Location='Remote')
    exp_to_csv(filtered_jobs)