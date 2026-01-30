# ATS Integration Microservice

## Project Overview
This project is an ATS (Applicant Tracking System) Integration Microservice developed using Django and Django REST Framework.  
It provides a unified REST API to manage jobs, candidates, and applications while integrating with an external ATS such as Zoho Recruit.

The goal of this service is to abstract ATS-specific logic and expose standardized endpoints that can be easily consumed by frontend applications or other services.

---

## Tech Stack
- Python
- Django
- Django REST Framework
- MySQL (SQLite used for local development)
- Zoho Recruit (ATS)
- Git & GitHub

---

## Features
- Fetch job listings from the ATS
- Create candidates
- Apply candidates to jobs
- Unified and standardized JSON API responses
- Clean separation of business logic using a service layer

---

## API Endpoints

### Get Jobs
**GET** `/api/jobs/`

**Response**
```json
[
  {
    "id": "job_1",
    "title": "Backend Developer",
    "location": "Remote",
    "status": "OPEN",
    "external_url": "https://example.com/job_1"
  }
]
