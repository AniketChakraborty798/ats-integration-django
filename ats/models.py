from django.db import models

class Job(models.Model):
    zoho_job_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    external_url = models.URLField()

class Candidate(models.Model):
    zoho_candidate_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Application(models.Model):
    zoho_application_id = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
