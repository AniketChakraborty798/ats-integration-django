ATS Integration Microservice
📌 Project Overview

This project is an ATS (Applicant Tracking System) Integration Microservice built using Django REST Framework.
It provides a unified REST API to manage jobs, candidates, and applications while integrating with an external ATS (Zoho Recruit).

The service abstracts ATS-specific logic and exposes standardized endpoints for easy consumption by frontend or third-party systems.

🛠️ Tech Stack

Backend: Python, Django

API Framework: Django REST Framework

Database: MySQL (SQLite used for local development)

ATS Integration: Zoho Recruit (via REST APIs)

Version Control: Git & GitHub

🚀 Features

Fetch job listings from the ATS

Create candidates

Apply candidates to jobs

Unified and standardized JSON responses

Clean service-layer abstraction for ATS logic

🔗 API Endpoints
1️⃣ Get Jobs

GET /api/jobs/

Response

[
  {
    "id": "job_1",
    "title": "Backend Developer",
    "location": "Remote",
    "status": "OPEN",
    "external_url": "https://example.com/job_1"
  }
]

2️⃣ Create Candidate

POST /api/candidates/

Request Body

{
  "name": "Aniket Chakraborty",
  "email": "aniket@email.com",
  "phone": "9999999999",
  "job_id": "job_1"
}


Response

{
  "message": "Candidate applied successfully"
}

3️⃣ Get Applications

GET /api/applications/?job_id=job_1

Response

[
  {
    "id": "app_1",
    "candidate_name": "Aniket Chakraborty",
    "email": "aniket@email.com",
    "status": "APPLIED"
  }
]

⚙️ Project Setup (Local)
1️⃣ Clone Repository
git clone https://github.com/<your-username>/ats-integration-django.git
cd ats_project

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver


Server will run at:

http://127.0.0.1:8000/

🔐 ATS Integration Notes

Zoho Recruit APIs are integrated via a dedicated service layer

OAuth-based authentication is supported

For local/demo purposes, ATS responses can be mocked

🧹 Git & Repository Hygiene

The following files/folders are excluded using .gitignore:

Virtual environment (venv/)

Python cache files (__pycache__/, *.pyc)

Local databases (db*.sqlite3)

Environment variables (.env)

📝 Assumptions

The project focuses on backend integration and API design

UI/Frontend is out of scope

SQLite is used for development; MySQL is intended for production

📄 Author

Aniket Chakraborty

✅ Conclusion

This project demonstrates how to design a scalable backend microservice that integrates with an external ATS while exposing clean, reusable REST APIs using Django.

