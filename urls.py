from django.urls import path
from .views import ( 
ApplicantDetailView,
EducationTypeView,
ExperienceView,
CourseView,
ProjectView,
SkillView,
CompanyView,
OpeningView,
SelectionView
)

urlpatterns = [
    path('', ApplicantDetailView.as_view()),
    path('education', EducationTypeView.as_view()),
    path('experience', ExperienceView.as_view()),
    path('course', CourseView.as_view()),
    path('project', ProjectView.as_view()),
    path('skill', SkillView.as_view()),
    path('company', CompanyView.as_view()),
    path('openings', OpeningView.as_view()),
    path('selection', SelectionView.as_view()),
]
