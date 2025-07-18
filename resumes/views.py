from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Resume
from .serializers import ResumeSerializer
from .parser import parse_resume
from resumes.utils import extract_skills_from_resume

class ResumeUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('resume')

        if not uploaded_file:
            return Response({"error": "No file uploaded."}, status=400)

        # Optional: Extract skills here using your utility function
        skills = extract_skills_from_resume(uploaded_file)

        # Save the file and create Resume instance
        resume = Resume.objects.create(file=uploaded_file, skills=skills)

        return Response({"resume_id": resume.id}, status=201)


class ResumeDetailView(APIView):
    permission_classes = []  # Open to all

    def get(self, request, pk):
        try:
            resume = Resume.objects.get(id=pk)
        except Resume.DoesNotExist:
            return Response({"error": "Resume not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResumeSerializer(resume)
        return Response(serializer.data)


class ResumeUpdateView(generics.UpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = []  # Open to all

    def perform_update(self, serializer):
        file = self.request.FILES.get('file')
        if file:
            from .parser import parse_resume
            text, skills, education, experience = parse_resume(file)
            serializer.save(
                parsed_text=text,
                skills=skills,
                education=education,
                experience=experience
            )
        else:
            serializer.save()


class ResumeDeleteView(generics.DestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = []  # Open to all
