from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ats.serializers import CandidateSerializer
from ats.services import (
    fetch_jobs,
    create_candidate,
    create_application,
    fetch_applications
)


class JobsView(APIView):
    def get(self, request):
        return Response(fetch_jobs())


class CandidateCreateView(APIView):
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        candidate = create_candidate(serializer.validated_data)
        create_application(
            candidate["id"],
            serializer.validated_data["job_id"]
        )

        return Response(
            {"message": "Candidate created and attached"},
            status=status.HTTP_201_CREATED
        )


class ApplicationsView(APIView):
    def get(self, request):
        job_id = request.query_params.get("job_id")
        return Response(fetch_applications(job_id))
