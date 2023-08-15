from django.db import models

# Create your models here.

class UpdateDataModel(models.Model):
    file = models.FileField()
    
class QueryBuilderModel(models.Model):
    Keyword = models.TextField(max_length=255)
    Industry = models.TextField(max_length=255)
    Year_Founded = models.DateField()
    City = models.TextField(max_length=255)
    State = models.TextField(max_length=255)
    Country = models.TextField(max_length=255)
    Employee_From = models.DateTimeField()
    Employee_To = models.DateTimeField()