from django.urls import path
from ats.views import JobsView, CandidateCreateView, ApplicationsView

urlpatterns = [
    path("jobs/", JobsView.as_view()),
    path("candidates/", CandidateCreateView.as_view()),
    path("applications/", ApplicationsView.as_view()),
]
