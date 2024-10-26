from django.db import models

class Interns(models.Model):
    Intern_name = models.CharField(max_length=200, null=True)
    Intern_id = models.CharField(max_length=200, null=True)
    Intern_salary = models.FloatField(default=0)
    def __str__(self)  :
        return self.Intern_name
   