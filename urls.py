from django.urls import path
from .views import ApplicantDetailView , SchoolView, ExperienceView, HigherView, CourseView, ProjectView, SkillView, CompanyView, OpeningView, SelectionView

urlpatterns = [
    path('', ApplicantDetailView.as_view()),
    path('secondary/', SchoolView.as_view()),
    path('higher/', HigherView.as_view()),
    path('experience/', ExperienceView.as_view()),
    path('course/', CourseView.as_view()),
    path('project/', ProjectView.as_view()),
    path('skill/', SkillView.as_view()),
    path('company/', CompanyView.as_view()),
    path('openings/', OpeningView.as_view()),
    path('selection/', SelectionView.as_view()),
]