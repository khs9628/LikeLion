from django.db import models
from django.urls import reverse


# Create your models here.
class Donkey(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('board:detail_donkey', arg=[self.id])

class Aicohol(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('board:detail_aicohol', arg=[self.id])


class Health(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('board:detail_health', arg=[self.id])


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

    