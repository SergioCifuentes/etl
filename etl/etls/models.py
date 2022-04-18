from django.db import models
from django.db.models.deletion import CASCADE



'''
database:
    1=postgres
    2=mysql
'''    
class Conection(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    database=models.IntegerField()
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    host=models.CharField(max_length=50)
    databaseName=models.CharField(max_length=50)
    port=models.IntegerField()
    
    

