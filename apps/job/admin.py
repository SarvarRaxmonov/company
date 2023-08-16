from django.contrib import admin
from apps.job.models import Vacancy, Resume, Company

# Register your models here.

admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(Vacancy)
