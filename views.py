from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework import generics
from .models import Applicant_Detail, School, Experience, Higher_Education, Course, Project, Skill, Company_Detail, No_Of_Opening, Selection_Rounds
from .serializers import ApplicantDetailSerializer, SchoolSerializer, ExperienceSerializer, HigherSerializer, CourseSerializer, ProjectSerializer, SkillSerializer, CompanyDetailSerializer, OpeningSerializer, SelectionRoundSerializer

class ApplicantDetailView(generics.ListCreateAPIView):
    queryset = Applicant_Detail.objects.all()
    serializer_class = ApplicantDetailSerializer
    permission_classes = (permissions.AllowAny, )

class SchoolView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (permissions.AllowAny, )

class HigherView(generics.ListCreateAPIView):
    queryset = Higher_Education.objects.all()
    serializer_class = HigherSerializer
    permission_classes = (permissions.AllowAny, )

class ExperienceView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (permissions.AllowAny, )

class CourseView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.AllowAny, )

class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny, )

class SkillView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (permissions.AllowAny, )

class CompanyView(generics.ListCreateAPIView):
    queryset = Company_Detail.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (permissions.AllowAny, )

class OpeningView(generics.ListCreateAPIView):
    queryset = No_Of_Opening.objects.all()
    serializer_class = OpeningSerializer
    permission_classes = (permissions.AllowAny, )

class SelectionView(generics.ListCreateAPIView):
    queryset = Selection_Rounds.objects.all()
    serializer_class = SelectionRoundSerializer
    permission_classes = (permissions.AllowAny, )
