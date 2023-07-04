from django.db import models
import datetime
# Create your models here.²

class FilmCateg(models.Model):

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Film(models.Model):

    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250)

    categs = models.ManyToManyField(FilmCateg)

    publish_date = models.DateField(default=datetime.date.today)

    poster = models.FileField(default=None)

    def __str__(self):
        return self.title + "  (" + str(self.publish_date.year) + ")"