from rest_framework.views import APIView
from rest_framework.response import Response
from resumes.models import Resume
from .utils import recommend_based_on_skills

class RecommendView(APIView):
    permission_classes = []

    def get(self, request, id):
        try:
            resume = Resume.objects.get(id=id)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found."}, status=404)

        skills = resume.skills or []
        recommendations = recommend_based_on_skills(skills)

        return Response({
            "resume_id": resume.id,
            "skills": skills,
            "recommendations": recommendations
        })
