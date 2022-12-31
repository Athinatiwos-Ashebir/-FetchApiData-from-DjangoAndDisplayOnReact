
from django.db import models

class DetailsModel(models.Model):
    id=models.AutoField(primary_key=True)
    stud_name=models.CharField(max_length=30)
    grade=models.CharField(max_length=5)
    
    def __str__(self):
        return self.stud_name or ''