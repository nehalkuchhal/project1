from django.contrib import admin
from .models import (
    School,
    Higher_Education,
    Applicant_Detail,
    Experience,
    Course,
    Project,
    Skill,
#company models
    Company_Detail,
    No_Of_Opening,
    Selection_Rounds
)
# Register your models here.

class SchoolInline(admin.TabularInline):
    model  = School

class HigherEducationInline(admin.TabularInline):
    model  = Higher_Education    



class ExperienceInline(admin.TabularInline):
    model  = Experience 

  

class CourseInline(admin.TabularInline):
    model  = Course  

class ProjectInline(admin.TabularInline):
    model  = Project  

class SkillInline(admin.TabularInline):
    model  = Skill  
    
@admin.register(Applicant_Detail)
class applicantdetailAdmin(admin.ModelAdmin):
    inlines =[

        SchoolInline,
        HigherEducationInline,  
        SkillInline,
        ExperienceInline,
        CourseInline,
        ProjectInline
    ]

class no_ofopeningInline(admin.TabularInline):
    model  = No_Of_Opening 

class SelectionInline(admin.TabularInline):
    model  = Selection_Rounds 

@admin.register(Company_Detail)
class CompanydetailAdmin(admin.ModelAdmin):
    inlines =[
       no_ofopeningInline,
       SelectionInline
    ]
