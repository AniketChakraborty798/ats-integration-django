def fetch_jobs():
    return [
        {
            "id": "job_1",
            "title": "Backend Developer",
            "location": "Remote",
            "status": "OPEN",
            "external_url": "https://example.com/job_1"
        }
    ]


def create_candidate(data):
    return {"id": "candidate_123"}


def create_application(candidate_id, job_id):
    return {"status": "created"}


def fetch_applications(job_id):
    return [
        {
            "id": "app_1",
            "candidate_name": "Aniket Chakraborty",
            "email": "aniket@email.com",
            "status": "APPLIED"
        }
    ]
