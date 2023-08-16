from rest_framework.response import Response

from apps.job.models import Vacancy, Company, Resume
from rest_framework import viewsets


# Create your views here.



class FilterViewSet(viewsets.ModelViewSet):

        def get(self, request, format=None):
            vacancy_count = Vacancy.objects.count()
            company_count = Company.objects.count()
            resume_count = Resume.objects.count()

            data = {
                'vacancies_count': vacancy_count,
                'companies_count': company_count,
                'resumes_count': resume_count,
            }

            return Response(data)

