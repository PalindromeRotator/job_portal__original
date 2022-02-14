from django.db import models
from email.policy import default

# Create your models here.
class User(models.Model):
    profile_picture = models.ImageField(null=False, blank=True, default='user.png')
    username = models.CharField(max_length=30, null=False, blank=False)
    firstname = models.CharField(max_length=30, null=False, blank=False, default="n/a")
    lastname = models.CharField(max_length=30, null=False, blank=False)
    gender = models.CharField(max_length=30, null=False, default="default")
    phone = models.IntegerField(default='0')
    skills = models.CharField(max_length=100, null=False, default="n/a")
    achievements = models.CharField(max_length=100, null=False, default="n/a")
    job_type = models.CharField(max_length=30, null=False, default="all")
    email = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.username

class Job(models.Model):
    job_title = models.CharField(max_length=30, null=False, blank=False)
    job_type = models.CharField(max_length=30, null=False, blank=False)
    job_details = models.CharField(max_length=30, null=False, blank=False,default="n/a")
    skills = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    company_id = models.IntegerField(default='0')
    job_id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.job_title

class Company(models.Model):
    company_name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=30, null=False, blank=False)
    email= models.CharField(max_length=30, null=True, blank=False)
    password = models.CharField(max_length=30, null=True, blank=False)
    company_id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.company_name

class Job_list(models.Model):
    full_name = models.CharField(max_length=30, null=True, blank=False)
    job_title = models.CharField(max_length=30, null=False, blank=False)
    job_type = models.CharField(max_length=30, null=False, blank=False)
    job_details = models.CharField(max_length=30, null=False, blank=False,default="n/a")
    skills = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    company_id = models.IntegerField(default='0')
    job_id_get = models.IntegerField(default='0')
    user_id_get = models.IntegerField(default='0')
    job_id = models.BigAutoField(primary_key=True)
    
    def __str__(self):
        return self.job_title
