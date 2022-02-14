from django.contrib import admin

# Register your models here.
from .models import User
from .models import Job
from .models import Company
from .models import Job_list

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Job_list)