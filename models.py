from django.db import models
from datetime import datetime

# Create your models here.


class Applicant_Detail(models.Model):
    name = models.CharField( max_length=150)
    mobile_number = models.IntegerField(blank=False)
    current_city = models.CharField( max_length=50)
    secondary = models.BooleanField(default=False)
    senior_secondary = models.BooleanField(default=False)
    higher = models.BooleanField(default=False)
    pg = models.BooleanField(default=False)
    diploma = models.BooleanField(default=False)
    phd = models.BooleanField(default=False)
    class Meta:
        verbose_name = (" Applicant_Detail")
        verbose_name_plural = ("Applicant_Details ")
        
    
    def __str__(self):
        return self.name

class School(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    #Education = models.ForeignKey(Education, on_delete=models.RESTRICT)
    pursuing = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    school_name = models.CharField(max_length=100)
    year_of_completion = models.IntegerField(blank = False)
    board = models.CharField(max_length=50)
    cgpa = models.FloatField(blank = False)
    percentage =  models.IntegerField(blank = False)

    class Meta:
        verbose_name = ("School")
        verbose_name_plural = ("Schools")

    def __str__(self):
        return self.school_name


class Higher_Education(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    #Education = models.ForeignKey(Education, on_delete=models.RESTRICT)
    pursuing = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    college_name = models.CharField(max_length=100)
    year_of_completion = models.IntegerField(blank = False)
    degree = models.CharField(max_length=50)
    stream = models.CharField(max_length=50)
    cgpa = models.FloatField(blank = False)
    percentage =  models.IntegerField(blank = False)

    class Meta:
        verbose_name = ("Higher Education")
        verbose_name_plural = ("Higher Education")

    def __str__(self):
        return self.college_name


class Experience(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    profile = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    work_from_home = models.BooleanField(default=False)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField( auto_now=False, auto_now_add=False)
    work_description = models.TextField(max_length=500)
    class Meta:
        verbose_name = (" Job")
        verbose_name_plural = ("Jobs")


class Course(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    course_name = models.CharField(max_length=500)
    organization = models.CharField(max_length=500)
    online = models.BooleanField(default=False)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=500)
    class Meta:
        verbose_name = (" Course")
        verbose_name_plural = ("Courses")

class Project(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    title = models.CharField(max_length=500)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField( auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=500)
    project_link = models.CharField(max_length=500)
    class Meta:
        verbose_name = (" Project")
        verbose_name_plural = ("Projects")
    
class Skill(models.Model):
    applicant_name = models.ForeignKey(Applicant_Detail, on_delete=models.RESTRICT)
    name = models.CharField(max_length=500)
    beginner = models.BooleanField(default=False)
    intermediate = models.BooleanField(default=False)
    advance = models.BooleanField(default=False)
    class Meta:
        verbose_name = (" skill")
        verbose_name_plural = ("skills")

#company detail
 
class Company_Detail(models.Model):
    about = models.TextField( max_length=150)
    oppurtunity_offered = models.TextField(max_length=150)
    skills_required = models.CharField( max_length=50)
    whocanaaply =  models.TextField(max_length=150)
    perks =  models.TextField(max_length=150)
    additional_info =  models.TextField(max_length=150)
    class Meta:
        verbose_name = (" Company_detail")
        verbose_name_plural = (" Company_details")

    def __str__(self):
        return self.oppurtunity_offered

class No_Of_Opening(models.Model):
    oppurtunity_offered = models.ForeignKey(Company_Detail, on_delete=models.RESTRICT)
    interns = models.IntegerField(blank = False)
    j_wd = models.IntegerField(blank = False)
    s_wd = models.IntegerField(blank = False)

class Selection_Rounds(models.Model):
    oppurtunity_offered = models.ForeignKey(Company_Detail, on_delete=models.RESTRICT)
    assessment = models.CharField( max_length=50)
    apptitude_test = models.CharField( max_length=50)
    coding_test = models.CharField( max_length=50)
    gd = models.CharField( max_length=50)
    interview_rounds = models.IntegerField(blank = False)
   
    class Meta:
        verbose_name = (" Selection")
        verbose_name_plural = (" Selection")
    





    




