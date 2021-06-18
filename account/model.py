from django.db import models
from datetime import datetime

# Create your models here.


class applicant_detail(models.Model):
    Name = models.CharField( max_length=150)
    Mobile_number = models.IntegerField(blank=False)
    Current_City = models.CharField( max_length=50)
    class Meta:
        verbose_name = (" applicant_detail")
        verbose_name_plural = (" applicant_details")
    
    def __str__(self):
        return self.Name

class Education(models.Model):
    Education = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    School = models.BooleanField(default=False)
    #name = models.CharField(max_length=50)
    Senior_Secondary = models.BooleanField(default=False)
    Higher = models.BooleanField(default=False)
    Pg = models.BooleanField(default=False)
    Diploma = models.BooleanField(default=False)
    Phd = models.BooleanField(default=False)
    class Meta:
        verbose_name = (" Education")
        verbose_name_plural = (" Education")
    

class School(models.Model):
    Education = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    #Education = models.ForeignKey(Education, on_delete=models.RESTRICT)
    Pursuing = models.BooleanField(default=False)
    Completed = models.BooleanField(default=False)
    School_Name = models.CharField(max_length=100)
    Year_of_Completion = models.IntegerField(blank = False)
    Board = models.CharField(max_length=50)
    Cgpa = models.IntegerField(blank = False)
    Percentage =  models.IntegerField(blank = False)

    class Meta:
        verbose_name = ("School")
        verbose_name_plural = ("Schools")

    def __str__(self):
        return self.School_Name


class Higher_Education(models.Model):
    Education = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    #Education = models.ForeignKey(Education, on_delete=models.RESTRICT)
    Pursuing = models.BooleanField(default=False)
    Completed = models.BooleanField(default=False)
    College_Name = models.CharField(max_length=100)
    Year_of_Completion = models.IntegerField(blank = False)
    Degree = models.CharField(max_length=50)
    Stream = models.CharField(max_length=50)
    Cgpa = models.IntegerField(blank = False)
    Percentage =  models.IntegerField(blank = False)

    class Meta:
        verbose_name = ("Higher Education")
        verbose_name_plural = ("Higher Education")

    def __str__(self):
        return self.College_Name


class Job(models.Model):
    Job_Detail = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    Profile = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    Work_from_Home = models.BooleanField(default=False)
    Start_Date = models.DateField( auto_now=False, auto_now_add=False)
    End_Date = models.DateField( auto_now=False, auto_now_add=False)
    work_description = models.TextField(max_length=500)
    class Meta:
        verbose_name = (" Job")
        verbose_name_plural = ("Jobs")

class Internship(models.Model):
    Internship_Detail = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    Profile = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    Work_from_Home = models.BooleanField(default=False)
    Start_Date = models.DateField( auto_now=False, auto_now_add=False)
    End_Date = models.DateField( auto_now=False, auto_now_add=False)
    work_description = models.TextField(max_length=500)
    class Meta:
        verbose_name = (" Internship")
        verbose_name_plural = ("Internships")

class Course(models.Model):
    Course_Detail = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    course_name = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    online = models.BooleanField(default=False)
    Start_Date = models.DateField( auto_now=False, auto_now_add=False)
    End_Date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=500)
    class Meta:
        verbose_name = (" Course")
        verbose_name_plural = ("Courses")

class Project(models.Model):
    Project_Detail = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    Title = models.CharField(max_length=500)
    Start_Date = models.DateField( auto_now=False, auto_now_add=False)
    End_Date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=500)
    project_link = models.CharField(max_length=500)
    class Meta:
        verbose_name = (" Project")
        verbose_name_plural = ("Projects")
    
class skill(models.Model):
    skill_Level = models.ForeignKey(applicant_detail, on_delete=models.RESTRICT)
    name = models.CharField(max_length=500)
    Beginner = models.BooleanField(default=False)
    Intermediate = models.BooleanField(default=False)
    Advance = models.BooleanField(default=False)
    class Meta:
        verbose_name = (" skill")
        verbose_name_plural = ("skills")

#company detail
 
class Company_detail(models.Model):
    About = models.TextField( max_length=150)
    Oppurtunity_offered = models.TextField(max_length=150)
    Skills_Required = models.CharField( max_length=50)
    whocanaaply =  models.TextField(max_length=150)
    perks =  models.TextField(max_length=150)
    additional_info =  models.TextField(max_length=150)
    class Meta:
        verbose_name = (" Company_detail")
        verbose_name_plural = (" Company_details")

class no_of_opening(models.Model):
    Opening_Detail = models.ForeignKey(Company_detail, on_delete=models.RESTRICT)
    Intern = models.IntegerField(blank = False)
    j_wd = models.IntegerField(blank = False)
    s_wd = models.IntegerField(blank = False)

class Selection_Rounds(models.Model):
    Selection_detail = models.ForeignKey(Company_detail, on_delete=models.RESTRICT)
    assessment = models.CharField( max_length=50)
    apptitude_test = models.CharField( max_length=50)
    coding_test = models.CharField( max_length=50)
    gd = models.CharField( max_length=50)
    interview_rounds = models.IntegerField(blank = False)
   
    class Meta:
        verbose_name = (" Selection")
        verbose_name_plural = (" Selection")
    




