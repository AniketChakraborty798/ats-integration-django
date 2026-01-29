from rest_framework import serializers

class CandidateSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    resume_url = serializers.URLField()
    job_id = serializers.CharField()
