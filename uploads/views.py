from rest_framework import generics
from .models import Resume
from .serializers import ResumeSerializer

class ResumeUploadView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer



from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Resume Uploader API 🚀</h1><p>Use /api/uploads/ resumes.</p>")









































































'''from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ResumeSerializer


class ResumeUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Resume uploaded successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''











'''class ResumeUploadView(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





from django.shortcuts import render
from rest_framework.response import responses
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ResumeSerializer


# Create your views here.


class ResumeUploadView(APIView):
    def post(self , request):
        serializer = ResumeSerializer(data = request.data)

        if serializer .is_valid():
            serializer.save()
            return responses(serializer.data , status = status.HTTP_201_CREATED)
        else:
            return responses(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''