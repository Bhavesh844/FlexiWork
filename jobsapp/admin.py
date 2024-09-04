from django.contrib import admin
from jobsapp.models import Job
from jobsapp.models import Applicant

# Register your models here.
admin.site.register(Job)
admin.site.register(Applicant)