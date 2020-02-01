from django.contrib import admin
from jobsapp.models import IndiaJobs

# Register your models here.
class IndiaJobsAdmin(admin.ModelAdmin):
    list_display = ['title','company','location','experience','salary']

admin.site.register(IndiaJobs,IndiaJobsAdmin)
