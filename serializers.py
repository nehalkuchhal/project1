from rest_framework import serializers
from .models import (
Applicant_Detail,
Education_Type,
Experience,
Course, 
Project,
Skill,
Company_Detail,
No_Of_Opening,
Selection_Rounds
)

class ApplicantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant_Detail
        fields = '__all__'

class EducationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_Type
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_Detail
        fields = '__all__'

class OpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = No_Of_Opening
        fields = '__all__'

class SelectionRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection_Rounds
        fields = '__all__'
