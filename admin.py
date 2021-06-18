from django.contrib import admin
from .models import (
    School,
    Higher_Education,
    Education,
    applicant_detail,
    Job,
    Internship,
    Course,
    Project,
    skill,
#company models
    Company_detail,
    no_of_opening,
    Selection_Rounds
)
# Register your models here.

class SchoolInline(admin.TabularInline):
    model  = School

class HigherEducationInline(admin.TabularInline):
    model  = Higher_Education    

class EducationInline(admin.TabularInline):
    model  = Education  

class JobInline(admin.TabularInline):
    model  = Job 

class InternshipInline(admin.TabularInline):
    model  = Internship  

class CourseInline(admin.TabularInline):
    model  = Course  

class ProjectInline(admin.TabularInline):
    model  = Project  

class skillInline(admin.TabularInline):
    model  = skill  
    
@admin.register(applicant_detail)
class applicantdetailAdmin(admin.ModelAdmin):
    inlines =[
        EducationInline,
        SchoolInline,
        HigherEducationInline,  
        skillInline,
        JobInline ,
        InternshipInline,
        CourseInline,
        ProjectInline
    ]

class no_ofopeningInline(admin.TabularInline):
    model  = no_of_opening 

class SelectionInline(admin.TabularInline):
    model  = Selection_Rounds 

@admin.register(Company_detail)
class CompanydetailAdmin(admin.ModelAdmin):
    inlines =[
       no_ofopeningInline,
       SelectionInline
    ]
