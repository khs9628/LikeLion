from django.db import models

# Create your models here.
class Blog(models.Model):
    donkey_title = models.CharField(max_length=200 , blank = True)
    donkey_name = models.CharField(max_length=50, blank = True)
    donkey_content = models.TextField()
    donkey_hits = models.IntegerField(null = True ,blank = True)
    donkey_time = models.DateTimeField('date published')
