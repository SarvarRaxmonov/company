from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    name = models.CharField(max_length=500)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

